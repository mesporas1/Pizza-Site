# Generated by Django 2.0.3 on 2019-07-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_orderdetail_topping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='topping',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
    ]