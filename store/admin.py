from django.contrib import admin
from store import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...