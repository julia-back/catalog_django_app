from django.contrib import admin
from .models import Category, Product, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "description")
    search_fields = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "price", "category")
    list_filter = ("category", )
    search_fields = ("name", "description")


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):

    list_display = ("city", "phone_number")
    search_fields = ("city", )
