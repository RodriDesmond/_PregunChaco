# Generated by Django 3.2.6 on 2021-09-02 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_perfil_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='password',
        ),
    ]