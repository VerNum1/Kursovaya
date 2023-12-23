import random

from homepage.models import *


def __generate_sfc():
    name = ['Bogdan', 'Matvey', 'Ivan', 'Eve', 'Juliana', 'Makar', 'Irina', 'Rostislav', 'Vasilisa']
    return (name[random.randint(0, len(name) - 1)] + '.' + name[random.randint(0, len(name) - 1)][0] + '.' +
            name[random.randint(0, len(name) - 1)][0])


def __generate_address():
    name = ['Seafield', 'Withers', 'Ivanov', 'Ramsgate', 'Story', 'Noviy', 'Newport', 'Shorokhova']
    return name[random.randint(0, len(name) - 1)] + ' st. ' + str(random.randint(1, 100))


def __generate_prof():
    name = ['The mathematician', 'Linguist', 'Physicist', 'Informatics', 'Chemist', 'Biologist']
    return name[random.randint(0, len(name) - 1)]


def __generate_homework():
    name = ['Exercise', 'Question number', 'Test']
    return name[random.randint(0, len(name) - 1)] + str(random.randint(0, 50))


def __generate_datetime():
    y = str(random.randint(2020, 2024))
    mo = str(random.randint(1, 12))
    d = str(random.randint(1, 28))
    h = str(random.randint(8, 20))
    mi = str(random.randint(0, 59))
    s = str(random.randint(0, 59))
    if int(h) < 10:
        h = '0' + h
    if int(mi) < 10:
        mi = '0' + mi
    if int(s) < 10:
        s = '0' + s

    return y + '-' + mo + '-' + d + ' ' + h + ':' + mi


def generate_contact(contact_id):
    return Contact(id=contact_id, sfc=__generate_sfc(), phone_num=random.randint(79000000000, 79999999999),
                   address=__generate_address())


def generate_customer(customer_id, cont_id):
    return Customers(id=customer_id, contact_id=cont_id)


def generate_tutor(tutors_id, cont_id):
    return Tutors(id=tutors_id, contact_id=cont_id, profession=__generate_prof())


def generate_timetable(tt_id, cus, tut):
    return Timetable(id=tt_id, meet_date=__generate_datetime(), homework=__generate_homework(), customer=cus,
                     tutor=tut)
