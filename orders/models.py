from django.db import models
from django.core.validators import MinValueValidator

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


