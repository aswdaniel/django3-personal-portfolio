# Generated by Django 3.0.6 on 2020-05-19 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='discription',
            new_name='description',
        ),
    ]
