from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

'''TYPES = ( ('SIC', 'Sicilian'), ('REG', 'Regular'))
SIZES = ( ('S', 'Small'), ('L', 'Large'))'''

'''class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    type = models.CharField(max_length = 3, choices = TYPES)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    size = models.CharField(max_length = 1, choices = SIZES)
    CHEESE = '0'
    ONE = '1'
    TWO = '2'
    THREE = '3'
    SPECIAL = 'X'
    numTOPPINGS = ( (CHEESE, 'Cheese'), (ONE, '1 Topping'), (TWO, '2 Toppings'), (THREE, '3 Toppings'), (SPECIAL, 'Special'))
    numToppings = models.CharField(max_length = 1, choices = numTOPPINGS, default = CHEESE)

    def __str__(self):
        return f"{self.size} {self.type} {self.numToppings} pizza: price {self.price}"

class Sub(models.Model):
    type = models.CharField(max_length=64)
    size = models.CharField(max_length = 1, choices = SIZES)
    price = models.DecimalField(max_digits = 10, decimal_places=2)


    def __str__(self):
        return f"{self.size} {self.type} sub: price {self.price}"
        
class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length = 1, choices = SIZES)
    price = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"{self.size} {self.name} dinnerPlatter: price {self.price}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"{self.name}: price {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"{self.name}: price {self.price}"
'''

class Food(models.Model):
    
    type = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits = 10, decimal_places=2,validators=[MinValueValidator(0)])
    size = models.CharField(max_length = 64)
    options = (('true', 'Yes'), ('false', 'No'))
    hasToppings = models.CharField(max_length = 5, choices = options, default = 'false')
    numToppings = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return f"{self.size} {self.type} price {self.price} has toppings: {self.hasToppings} number of toppings: {self.numToppings}"