from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
        migrations.AlterModelOptions(
            name='tutors',
            options={'verbose_name': 'Репетитор', 'verbose_name_plural': 'Репетиторы'},
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Расписание'},
        ),
    ]