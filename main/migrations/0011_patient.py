# Generated by Django 3.1 on 2020-10-01 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_booked_schedule'),
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
            ],
        ),
    ]
