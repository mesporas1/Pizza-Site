# Generated by Django 2.0.3 on 2019-07-25 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0017_auto_20190723_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cart', to='orders.Cart')),
                ('food', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='CartFood', to='orders.Food')),
                ('topping', models.ManyToManyField(blank=True, related_name='CartTopping', to='orders.Topping')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserOrder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='food',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='OrderFood', to='orders.Food'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='topping',
            field=models.ManyToManyField(blank=True, related_name='OrderTopping', to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cartdetails',
            field=models.ManyToManyField(through='orders.CartDetail', to='orders.Food'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserCart', to=settings.AUTH_USER_MODEL),
        ),
    ]
