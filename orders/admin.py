from django.contrib import admin

from .models import Food, Item, Size,Topping,Order,OrderDetail
# Register your models here.

class FoodLineItem(admin.StackedInline):
    model = OrderDetail.foods.through
    extra = 1

class OrderDetailAdmin(admin.ModelAdmin):
    inlines = [FoodLineItem]

'''class FoodAdmin(admin.ModelAdmin):
    filter_horizontal = ("name",)'''

'''admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(DinnerPlatter)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Topping)'''
admin.site.register(Food)
admin.site.register(Item)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(OrderDetail, OrderDetailAdmin)