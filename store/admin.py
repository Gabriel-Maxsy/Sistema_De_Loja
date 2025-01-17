from django.contrib import admin
from store import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'category', 'price',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'price',
    list_display_links = 'id', 'name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...