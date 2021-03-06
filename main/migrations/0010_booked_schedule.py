# Generated by Django 3.1 on 2020-09-29 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_expertprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Free', 'Free'), ('Booked', 'Booked')], default='Free', max_length=30)),
                ('docprof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctorprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('timing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.schedule')),
            ],
        ),
    ]
