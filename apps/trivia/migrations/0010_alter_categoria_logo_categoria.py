# Generated by Django 3.2.6 on 2021-09-01 14:49

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0009_alter_categoria_logo_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='logo_categoria',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/Users/Summer/Documents/GitHub/_PregunChaco/media'), upload_to=''),
        ),
    ]
