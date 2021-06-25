# Generated by Django 3.1.6 on 2021-06-25 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0006_auto_20210624_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='devotee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='church.devotee'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='proof_payment',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/Devotee/'),
        ),
    ]
