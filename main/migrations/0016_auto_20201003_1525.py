# Generated by Django 3.1 on 2020-10-03 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20201003_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='broad',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='narrow',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='docprof',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='docprof',
        ),
        migrations.DeleteModel(
            name='Booked',
        ),
        migrations.DeleteModel(
            name='DoctorProfile',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]