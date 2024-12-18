from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Product, Contacts


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"


class ProductDetailView(DetailView):
    model = Product


class ContactsView(View):

    def get(self, request):
        contacts = Contacts.objects.all()
        context = {"object_list": contacts}
        return render(request, "catalog/contacts_list.html", context=context)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name} ({email})! Ваше сообщение получено. ({message})")
