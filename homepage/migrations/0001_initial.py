from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sfc', models.CharField(max_length=255)),
                ('phone_num', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Tutors',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('profession', models.CharField(max_length=100)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('meet_date', models.DateTimeField()),
                ('homework', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.customers')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.tutors')),
            ],
        ),
    ]