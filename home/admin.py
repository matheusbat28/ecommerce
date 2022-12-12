from django.contrib import admin
from .models import Product, Category, Image, cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description', 'size')
    list_filter = ('name', 'value', 'description', 'size')
    search_fields = ('name', 'value', 'description', 'size')
    list_per_page = 25
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    list_filter = ('image',)
    search_fields = ('image',)
    list_per_page = 25
    
class CartAdmin(admin.ModelAdmin):
    list_display = ('id_user',)
    list_filter = ('id_user',)
    search_fields =('id_user',)
    list_per_page = 25
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(cart, CartAdmin)