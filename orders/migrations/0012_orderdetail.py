# Generated by Django 2.0.3 on 2019-07-19 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20190719_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foods', models.ManyToManyField(to='orders.Food')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order', to='orders.Order')),
                ('toppings', models.ManyToManyField(to='orders.Topping')),
            ],
        ),
    ]

    
