# Generated by Django 3.1.6 on 2021-06-25 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0007_auto_20210625_0534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='proof_payment',
        ),
        migrations.AddField(
            model_name='donation',
            name='bank_method',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='donation',
            name='gcash_method',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='seat',
            name='devotee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='church.booking'),
        ),
    ]
