from django.contrib import admin

from .models import Customer
from .models import Product
from .models import Bill
from .models import Order
from .models import ProductType

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter=['first_name']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(ProductType)