# Generated by Django 2.0.3 on 2019-07-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_food_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(default='None', help_text='Do not include size in name', max_length=64),
        ),
        migrations.AlterField(
            model_name='food',
            name='numToppings',
            field=models.PositiveIntegerField(default=0, help_text='0 for cheese pizza'),
        ),
    ]