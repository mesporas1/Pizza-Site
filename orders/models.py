from django.db import models

# Create your models here.

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    type = models.CharField(max_length=64)
    size = models.CharField(max_length=32)
    price = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"{self.size} {self.type} pizza: price {self.price}"

class Sub(models.Model):
    type = models.CharField(max_length=64)
    size = models.CharField(max_length=32)
    price = models.DecimalField(max_digits = 10, decimal_places=2)


    def __str__(self):
        return f"{self.size} {self.type} sub: price {self.price}"
        
class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=32)
    price = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"{self.size} {self.name} dinnerPlatter: price {self.price}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"{self.name}: price {self.price}"

class Salads(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"{self.name}: price {self.price}"
