from django.urls import path
from . import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.ProductListView.as_view(), name="home"),
    path("contacts/", views.ContactsListView.as_view(), name="contacts"),
    # path("contacts/form/", views.ContactsFormView.as_view(), name="contacts_form"),
    path("product_detail/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    # path("thanks_for_message/", views.)
]
