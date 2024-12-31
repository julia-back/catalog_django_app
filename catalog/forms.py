from django.forms import Form, ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
