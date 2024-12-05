from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home_page(request):
    if request.method == "GET":
        return render(request, "catalog/home_page.html")


def contacts(request):
    if request.method == "GET":
        return render(request, "catalog/contacts.html")
    name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")
    return HttpResponse(f"Спасибо, {name}!\n Мы получили ваше сообщение {message}\n"
                        f"Ответ возможно придет на почту: {email}.")


def product_info(request, product_id):
    product = models.Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, "catalog/product_info.html", context=context)
