# Generated by Django 2.0.3 on 2019-07-05 18:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190705_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='numToppings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
