from django.shortcuts import render


def home_page(request):
    if request.method == "GET":
        return render(request, "catalog/templates/catalog/home_page.html")


def contacts(request):
    if request.method == "GET":
        return render(request, "catalog/templates/catalog/contacts.html")
