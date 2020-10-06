# Generated by Django 3.1 on 2020-10-03 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('complaint', models.CharField(max_length=100)),
                ('investigation', models.CharField(max_length=100)),
                ('examination', models.CharField(max_length=100)),
                ('docprof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctorprofile')),
            ],
        ),
    ]
