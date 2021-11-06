# Generated by Django 2.2.24 on 2021-11-06 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
