from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_id', 'slug', 'icon']
    list_display_links = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category', 'inventory', 'top_deal', 'flash_sales']
    list_display_links = ['name']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

