from django.contrib import admin
from .models import Product,Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('name','category','description')
        }),
        ('Size & Price',{
            'fields':('size','price','price_medium','price_large')
        }),
        ('Image & Created',{
            'fields':('image','created')
        }),
    )
    list_display = ('name','description','price')
    list_editable = ('description','price')
    list_filter = ('name','price')
    readonly_fields = ('created',)


admin.site.register(Category)


# Register your models here.
