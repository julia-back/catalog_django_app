from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Contacts, Category
from django.urls import reverse_lazy
from .forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .services import get_product_from_cache_or_db
from django.core.cache import cache
from config.settings import CACHE_ENABLED


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"

    def get_queryset(self):
        if CACHE_ENABLED:
            products_queryset = cache.get("product_list_queryset")
            if not products_queryset:
                products_queryset = Product.objects.all()
                cache.set("product_list_queryset", products_queryset, 60 * 15)
            return products_queryset
        products_queryset = Product.objects.all()
        return products_queryset


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete_form.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.delete_product"


class ContactsView(LoginRequiredMixin, View):

    def get(self, request):
        contacts = Contacts.objects.all()
        context = {"object_list": contacts}
        return render(request, "catalog/contacts.html", context=context)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name} ({email})! Ваше сообщение получено. ({message})")


class CategoryListView(ListView):
    model = Category


class ProductListByCategory(ListView):
    model = Product
    template_name = "catalog/product_by_category.html"

    def get_queryset(self):
        category = self.kwargs.get("pk_category")
        product_by_category = get_product_from_cache_or_db(category)
        return product_by_category
