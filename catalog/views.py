from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Product, Contacts
from .forms import ContactsForm
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"


class ProductDetailView(DetailView):
    model = Product


class ContactsListView(ListView):
    model = Contacts


# class ContactsFormView(FormView):
#     form_class = ContactsForm
#     success_url = reverse_lazy("catalog:home")
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
