from django.urls import path
from . import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("home_page/", views.home_page, name="home_page"),
    path("contacts/", views.contacts, name="contacts"),
    path("product_info/<int:product_id>", views.product_info, name="product_info")
]
