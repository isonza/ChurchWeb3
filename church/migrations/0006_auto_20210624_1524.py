# Generated by Django 3.1.6 on 2021-06-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0005_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='proof_payment',
            field=models.ImageField(blank=True, null=True, upload_to='proof_payment/Payment/'),
        ),
    ]
