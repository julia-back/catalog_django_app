from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Contacts
from django.urls import reverse_lazy
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete_form.html"
    success_url = reverse_lazy("catalog:home")


class ContactsView(View):

    def get(self, request):
        contacts = Contacts.objects.all()
        context = {"object_list": contacts}
        return render(request, "catalog/contacts.html", context=context)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name} ({email})! Ваше сообщение получено. ({message})")
