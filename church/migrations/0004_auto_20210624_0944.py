# Generated by Django 3.1.6 on 2021-06-24 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0003_auto_20210624_0546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covid',
            old_name='COVID_INTERACTION',
            new_name='COVID_positive_interaction',
        ),
        migrations.RenameField(
            model_name='covid',
            old_name='AREA',
            new_name='high_COVID_area',
        ),
        migrations.RenameField(
            model_name='covid',
            old_name='HAVE_FEVER',
            new_name='symptoms',
        ),
        migrations.RenameField(
            model_name='covid',
            old_name='OUTSIDE_TRAVEL',
            new_name='travel_outside',
        ),
    ]