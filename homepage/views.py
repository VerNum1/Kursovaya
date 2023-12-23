import csv
import io
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import TableStyle, Table, SimpleDocTemplate

from homepage.generate import *
from homepage.forms import *
from homepage.models import *


def homepage(request):
    return render(request, "homepage/index.html")


def sign(request):
    form_log = AddLoginForm()
    form_reg = AddRegisterForm()

    if request.method == 'POST':
        form_log = AddLoginForm(request.POST)
        form_reg = AddRegisterForm(request.POST)
        if form_log.is_valid():
            print(form_log.cleaned_data)
            user = authenticate(username=form_log.cleaned_data.get("login"),
                                password=form_log.cleaned_data.get("password"))
            if user is not None:
                login(request, user)
                return redirect('homepage')
        if form_reg.is_valid():
            print(form_reg.cleaned_data)

            user = User.objects.create_user(form_reg.cleaned_data.get('login'), '',
                                            form_reg.cleaned_data.get('password1'))
            user.first_name = form_reg.cleaned_data.get('sfc')
            user.save()
            contact = Contact(sfc=form_reg.cleaned_data.get('sfc'), phone_num=form_reg.cleaned_data.get('phone_num'),
                              address=form_reg.cleaned_data.get('address'), user=user)
            contact.save()
            customer = Customers(contact_id=contact)
            customer.save()
            return redirect('login')

    return render(request, "homepage/logreg.html", {'fl': form_log, 'fr': form_reg})


def logout_user(request):
    logout(request)
    return redirect('login')


def tutors(request, profes='', tutor_id=''):
    if not request.user.is_authenticated:
        redirect('login')

    if profes == '':

        tuts = Tutors.objects.all()

        d = {}

        for tut in tuts:
            if tut.profession in d.keys():
                d[tut.profession] += 1
            else:
                d[tut.profession] = 1

        return render(request, "homepage/tutors.html", {'profs': d.keys()})
    elif tutor_id == '':

        tuts = Tutors.objects.filter(profession=profes)

        d = []

        class ch:
            def __init__(self, id, name):
                self.id = id
                self.name = name

        for tut in tuts:
            d.append(ch(tut.contact_id.id, tut.contact_id.sfc))

        return render(request, "homepage/tutors.html", {'profs': d, 'choose': profes})


def customers(request):
    return render(request, "homepage/customers.html")


def timetable(request):
    if not request.user.is_authenticated:
        redirect('login')

    if request.user.has_perm('homepage.view_timetable'):
        try:
            tut = Tutors.objects.get(contact_id=Contact.objects.get(user=request.user.id).id)
        except:
            return redirect('new_tut')

    if request.user.has_perm('homepage.view_timetable'):
        tut = Tutors.objects.get(contact_id=Contact.objects.get(user=request.user.id).id)
        TT = Timetable.objects.filter(tutor=tut)
    else:
        cus = Customers.objects.get(contact_id=Contact.objects.get(user=request.user.id).id)
        TT = Timetable.objects.filter(customer=cus)

    return render(request, "homepage/timetable.html", {'Tab': TT})


def generate(request):
    con = Contact.objects.all()
    cus = Customers.objects.all()
    tut = Tutors.objects.all()
    tim = Timetable.objects.all()

    con_c = con.count()
    cus_c = cus.count()
    tut_c = tut.count()
    tim_c = tim.count()

    for i in range(300):  # generate customers
        a = generate_contact(i + con_c)
        a.save()
        b = generate_customer(i + cus_c, a)
        b.save()

    con_c += 300
    cus_c += 300

    for i in range(50):  # generate tutors
        a = generate_contact(i + con_c)
        a.save()
        b = generate_tutor(i + tut_c, a)
        b.save()

    cus = Customers.objects.all()
    tut = Tutors.objects.all()
    cus_c = cus.count()
    tut_c = tut.count()

    for i in range(500):
        a = generate_timetable(i + tim_c, cus[random.randint(0, cus_c - 1)], tut[random.randint(0, tut_c - 1)])
        a.save()

    return HttpResponse('OK')


def download_pdf(request):
    cus = Customers.objects.get(contact_id=Contact.objects.get(user=request.user.id).id)
    TT = Timetable.objects.filter(customer=cus)

    response = HttpResponse(content_type='application/pdf')
    pdf_name = "timetable-%s.pdf" % str(cus.contact_id.sfc)
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name

    buff = io.StringIO()

    tut = SimpleDocTemplate(response, pagesize=letter, rightMargin=70, leftMargin=70, topMargin=70,
                            bottomMargin=60)
    elements = []

    data = [['Customer', 'Tutor', 'Date&Time', 'homeworks']]
    for i in TT:
        data.append([i.customer.contact_id.sfc, i.tutor.contact_id.sfc, i.meet_date, i.homeworks])
    t = Table(data)
    t.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                           ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                           ('VALIGN', (0, 0), (0, -1), 'TOP'),
                           ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                           ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                           ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                           ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                           ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                           ]))

    elements.append(t)
    # write the document to
    tut.build(elements)

    print(response.items())

    # response.write(buff.getvalue())
    # buff.close()
    return response


def download_csv(request):
    cus = Customers.objects.get(contact_id=Contact.objects.get(user=request.user.id).id)
    TT = Timetable.objects.filter(customer=cus)

    # Create the HttpResponse object with the appropriate CSV header.

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="timetable.csv"'},
    )

    writer = csv.writer(response, delimiter=';')
    for i in TT:
        writer.writerow([i.customer.contact_id.sfc, i.tutor.contact_id.sfc, i.meet_date, i.homeworks])

    return response


def appointment(request, profes, id):
    formTT = AppointmentForm()

    if request.method == 'POST':
        formTT = AppointmentForm(request.POST)
        if formTT.is_valid():
            print(formTT.cleaned_data.get('meet_date'))

            cus = Customers.objects.get(contact_id=Contact.objects.get(user=request.user.id).id)
            tut = Tutors.objects.get(contact_id=id)

            meet = Timetable(customer=cus, tutor=tut, meet_date=formTT.cleaned_data.get('meet_time'))
            meet.save()
            return redirect('/')
    return render(request, "homepage/appointment.html", {'ftt': formTT, 'profes': profes, 'id': id})


def new_tutor(request):
    form = AddTutProf()

    if request.method == 'POST':
        form = AddTutProf(request.POST)
        if form.is_valid():
            newd = Tutors(contact_id=Contact.objects.get(user=request.user.id),
                          profession=form.cleaned_data.get('prof'))
            newd.save()
            return redirect('timetable')

    return render(request, 'homepage/new_tut.html', {'f': form})


def change_homeworks(request, id):
    form = HomeForm()

    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            newd = Timetable.objects.get(id=id)
            newd.homeworks = form.cleaned_data.get('home')
            newd.save()
            return redirect('timetable')

    return render(request, 'homepage/new_home.html', {'f': form, 'id': id})
