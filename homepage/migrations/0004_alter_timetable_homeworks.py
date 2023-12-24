from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_contact_user_alter_contact_id_alter_customers_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='homework',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
