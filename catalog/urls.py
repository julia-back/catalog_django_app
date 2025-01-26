from django.urls import path
from . import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.ProductListView.as_view(), name="home"),
    path("product_detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("new_product/", views.ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update", views.ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete", views.ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("category_list/", views.CategoryListView.as_view(), name="category_list"),
    path("product_by_category/<int:pk_category>", views.ProductListByCategory.as_view(), name="product_by_category"),
]
