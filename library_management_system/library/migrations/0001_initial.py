# Generated by Django 3.2.9 on 2022-01-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('admin_email', models.CharField(max_length=20)),
                ('admin_address', models.CharField(max_length=20)),
                ('admin_number', models.IntegerField(max_length=20)),
                ('admin_passw', models.CharField(max_length=20)),
            ],
        ),
    ]
