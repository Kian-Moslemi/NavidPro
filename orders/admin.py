from django.contrib import admin
from .models import Order,Address


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('first_name','last_name')
        }),
        ('Phone & Postal_code & Email',{
            'fields':('phone','postal_code','email')
        }),
        ('User & Address',{
            'fields':('user','address')
        }),
    )
    list_display = ('first_name','last_name','postal_code','address')



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user','address_line')
    list_editable = ('address_line',)


# Register your models here.
