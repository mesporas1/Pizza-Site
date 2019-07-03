from django.contrib import admin

from .models import Pizza, Sub, DinnerPlatter, Pasta, Salad, Topping
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(DinnerPlatter)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Topping)