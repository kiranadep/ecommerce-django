# Generated by Django 4.2.14 on 2024-08-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_order_phone_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
