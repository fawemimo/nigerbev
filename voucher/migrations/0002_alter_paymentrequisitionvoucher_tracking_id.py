# Generated by Django 4.0.4 on 2022-05-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrequisitionvoucher',
            name='tracking_id',
            field=models.CharField(default='NBL/130/8/248', editable=False, max_length=20),
        ),
    ]
