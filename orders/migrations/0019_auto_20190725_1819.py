# Generated by Django 2.0.3 on 2019-07-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20190725_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cartdetails',
            field=models.ManyToManyField(blank=True, through='orders.CartDetail', to='orders.Food'),
        ),
    ]
