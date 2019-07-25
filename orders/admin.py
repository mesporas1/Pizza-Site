from django.contrib import admin

from .models import Food, Item, Size,Topping,Order,OrderDetail,Cart,CartDetail
# Register your models here.

class FoodLineItemOrder(admin.StackedInline):
    model = OrderDetail
    extra = 0

class OrderDetailAdmin(admin.ModelAdmin):
    inlines = [FoodLineItemOrder]

class FoodLineItemCart(admin.StackedInline):
    model = CartDetail
    extra = 0

class CartDetailAdmin(admin.ModelAdmin):
    inlines = [FoodLineItemCart]

'''class FoodAdmin(admin.ModelAdmin):
    filter_horizontal = ("name",)'''

admin.site.register(Food)
admin.site.register(Item)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Order, OrderDetailAdmin)
admin.site.register(Cart, CartDetailAdmin)