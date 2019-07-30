from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length = 64)
    
    def __str__(self):
        return f"{self.name}"

class Size(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.name}"

class Food(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="FoodItem")
    price = models.DecimalField(max_digits = 10, decimal_places=2,validators=[MinValueValidator(0)])
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="Size")
    options = (('true', 'Yes'), ('false', 'No'))
    hasToppings = models.CharField(max_length = 5, choices = options, default = 'false')
    numToppings = models.PositiveIntegerField(default = 0, help_text = "0 for cheese pizza")
    name = models.CharField(max_length = 64, default = "None", help_text = "Do not include size in name")
    def __str__(self):
        return f"{self.size} {self.name} Price {self.price}"

class Topping(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserOrder")
    orderdetails = models.ManyToManyField(Food, through = 'OrderDetail')
    total = models.DecimalField(max_digits = 10, decimal_places=2,validators=[MinValueValidator(0)], default = 0)
    def __str__(self):
        return f"Order#{self.id}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="Order")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="OrderFood", default = 0)
    quantity = models.PositiveIntegerField(default = 1)
    topping = models.ManyToManyField(Topping, blank = True, related_name="OrderTopping")
    
    def __str__(self):
        return f"All the foods: {self.food} {self.quantity}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserCart")
    cartdetails = models.ManyToManyField(Food, through = 'CartDetail', blank = True)
    total = models.DecimalField(max_digits = 10, decimal_places=2,validators=[MinValueValidator(0)], default = 0)
    def __str__(self):
        return f"Cart#{self.id}"


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="Cart")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="CartFood", default = 0)
    quantity = models.PositiveIntegerField(default = 1)
    topping = models.ManyToManyField(Topping, blank = True, related_name="CartTopping")
    
    def __str__(self):
        return f"All the foods: {self.food} {self.quantity}"