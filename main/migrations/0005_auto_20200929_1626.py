# Generated by Django 3.1 on 2020-09-29 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_country_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narrow',
            name='name',
            field=models.CharField(blank=True, default='Not Available', max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField()),
                ('address', models.TextField()),
                ('broad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.broad')),
                ('narrow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.narrow')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.state')),
            ],
        ),
    ]
