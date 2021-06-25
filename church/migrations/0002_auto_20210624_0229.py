# Generated by Django 3.1.6 on 2021-06-24 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('A1', models.BooleanField(default=True)),
                ('A2', models.BooleanField(default=True)),
                ('A3', models.BooleanField(default=True)),
                ('A4', models.BooleanField(default=True)),
                ('A5', models.BooleanField(default=True)),
                ('A6', models.BooleanField(default=True)),
                ('A7', models.BooleanField(default=True)),
                ('A8', models.BooleanField(default=True)),
                ('A9', models.BooleanField(default=True)),
                ('A10', models.BooleanField(default=True)),
                ('A11', models.BooleanField(default=True)),
                ('A12', models.BooleanField(default=True)),
                ('B1', models.BooleanField(default=True)),
                ('B2', models.BooleanField(default=True)),
                ('B3', models.BooleanField(default=True)),
                ('B4', models.BooleanField(default=True)),
                ('B5', models.BooleanField(default=True)),
                ('B6', models.BooleanField(default=True)),
                ('B7', models.BooleanField(default=True)),
                ('B8', models.BooleanField(default=True)),
                ('B9', models.BooleanField(default=True)),
                ('B10', models.BooleanField(default=True)),
                ('B11', models.BooleanField(default=True)),
                ('B12', models.BooleanField(default=True)),
                ('C1', models.BooleanField(default=True)),
                ('C2', models.BooleanField(default=True)),
                ('C3', models.BooleanField(default=True)),
                ('C4', models.BooleanField(default=True)),
                ('C5', models.BooleanField(default=True)),
                ('C6', models.BooleanField(default=True)),
                ('C7', models.BooleanField(default=True)),
                ('C8', models.BooleanField(default=True)),
                ('C9', models.BooleanField(default=True)),
                ('C10', models.BooleanField(default=True)),
                ('C11', models.BooleanField(default=True)),
                ('C12', models.BooleanField(default=True)),
                ('D1', models.BooleanField(default=True)),
                ('D2', models.BooleanField(default=True)),
                ('D3', models.BooleanField(default=True)),
                ('D4', models.BooleanField(default=True)),
                ('D5', models.BooleanField(default=True)),
                ('D6', models.BooleanField(default=True)),
                ('D7', models.BooleanField(default=True)),
                ('D8', models.BooleanField(default=True)),
                ('D9', models.BooleanField(default=True)),
                ('D10', models.BooleanField(default=True)),
                ('D11', models.BooleanField(default=True)),
                ('D12', models.BooleanField(default=True)),
                ('E1', models.BooleanField(default=True)),
                ('E2', models.BooleanField(default=True)),
                ('E3', models.BooleanField(default=True)),
                ('E4', models.BooleanField(default=True)),
                ('E5', models.BooleanField(default=True)),
                ('E6', models.BooleanField(default=True)),
                ('E7', models.BooleanField(default=True)),
                ('E8', models.BooleanField(default=True)),
                ('E9', models.BooleanField(default=True)),
                ('E10', models.BooleanField(default=True)),
                ('E11', models.BooleanField(default=True)),
                ('E12', models.BooleanField(default=True)),
                ('F1', models.BooleanField(default=True)),
                ('F2', models.BooleanField(default=True)),
                ('F3', models.BooleanField(default=True)),
                ('F4', models.BooleanField(default=True)),
                ('F5', models.BooleanField(default=True)),
                ('F6', models.BooleanField(default=True)),
                ('F7', models.BooleanField(default=True)),
                ('F8', models.BooleanField(default=True)),
                ('F9', models.BooleanField(default=True)),
                ('F10', models.BooleanField(default=True)),
                ('F11', models.BooleanField(default=True)),
                ('F12', models.BooleanField(default=True)),
                ('G1', models.BooleanField(default=True)),
                ('G2', models.BooleanField(default=True)),
                ('G3', models.BooleanField(default=True)),
                ('G4', models.BooleanField(default=True)),
                ('G5', models.BooleanField(default=True)),
                ('G6', models.BooleanField(default=True)),
                ('G7', models.BooleanField(default=True)),
                ('G8', models.BooleanField(default=True)),
                ('G9', models.BooleanField(default=True)),
                ('G10', models.BooleanField(default=True)),
                ('G11', models.BooleanField(default=True)),
                ('G12', models.BooleanField(default=True)),
                ('H1', models.BooleanField(default=True)),
                ('H2', models.BooleanField(default=True)),
                ('H3', models.BooleanField(default=True)),
                ('H4', models.BooleanField(default=True)),
                ('H5', models.BooleanField(default=True)),
                ('H6', models.BooleanField(default=True)),
                ('H7', models.BooleanField(default=True)),
                ('H8', models.BooleanField(default=True)),
                ('H9', models.BooleanField(default=True)),
                ('H10', models.BooleanField(default=True)),
                ('H11', models.BooleanField(default=True)),
                ('H12', models.BooleanField(default=True)),
                ('I1', models.BooleanField(default=True)),
                ('I2', models.BooleanField(default=True)),
                ('I3', models.BooleanField(default=True)),
                ('I4', models.BooleanField(default=True)),
                ('I5', models.BooleanField(default=True)),
                ('I6', models.BooleanField(default=True)),
                ('I7', models.BooleanField(default=True)),
                ('I8', models.BooleanField(default=True)),
                ('I9', models.BooleanField(default=True)),
                ('I10', models.BooleanField(default=True)),
                ('I11', models.BooleanField(default=True)),
                ('I12', models.BooleanField(default=True)),
                ('J1', models.BooleanField(default=True)),
                ('J2', models.BooleanField(default=True)),
                ('J3', models.BooleanField(default=True)),
                ('J4', models.BooleanField(default=True)),
                ('J5', models.BooleanField(default=True)),
                ('J6', models.BooleanField(default=True)),
                ('J7', models.BooleanField(default=True)),
                ('J8', models.BooleanField(default=True)),
                ('J9', models.BooleanField(default=True)),
                ('J10', models.BooleanField(default=True)),
                ('J11', models.BooleanField(default=True)),
                ('J12', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devotee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/Devotee/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='devotee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='church.devotee'),
        ),
        migrations.AlterField(
            model_name='covid',
            name='devotee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='church.devotee'),
        ),
        migrations.AlterField(
            model_name='prayertestimony',
            name='devotee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='church.devotee'),
        ),
    ]
