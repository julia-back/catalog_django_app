from django.db import models
from users.models import User


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"Категория '{self.name}'"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]
        db_table = "categories_table"


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    product_photo = models.ImageField(upload_to="product_photos/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Продукт '{self.name}'"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        db_table = "products_table"
        permissions = [("can_unpublish_product", "Can unpublish product"),]


class Contacts(models.Model):

    city = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city} {self.phone_number}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
        ordering = ["city"]
        db_table = "contacts_table"
