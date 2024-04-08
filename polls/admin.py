from django.contrib import admin
from polls.models import Menu, MenuCategory, Customer, Order

# Register your models here.
class MenuCategoryInline(admin.TabularInline):
    model = MenuCategory
    extra = 2
    list_display = ["menu_name", "price"]


class MenuAdmin(admin.ModelAdmin):
    list_display = ["menu"]
    inlines = [MenuCategoryInline]


class OrderInline(admin.TabularInline):
    model = Order
    extra = 2
    list_display = ["order_menu", "count", 'order_date']


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['phone_num']
    inlines = [OrderInline]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Customer, CustomerAdmin)