from django.urls import path
from . import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.ProductListView.as_view(), name="home"),
    path("product_detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", views.ContactsView.as_view(), name="contacts")
]
