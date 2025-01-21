from django.forms import ModelForm, ValidationError
from .models import Product


banned_worlds = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductModeratorForm(ModelForm):

    class Meta:
        model = Product
        fields = ["is_published"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get("is_published").widget.attrs.update({"class": "form-check"})


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["owner", "is_published"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field, value in self.fields.items():
            if field == "name":
                value.widget.attrs.update({"placeholder": "Введите название товара"})
                value.label = "Название продукта"
            if field == "description":
                value.widget.attrs.update({"placeholder": "Введите описание товара"})
                value.label = "Описание продукта"
            if field == "product_photo":
                value.label = "Фото продукта"
            if field == "category":
                value.label = "Категория"
            if field == "price":
                value.label = "Цена"
            value.widget.attrs.update({"class": "form-control"})
            if field == "is_published":
                value.widget.attrs.update({"class": "form-check"})

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if float(price) < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        for world in banned_worlds:
            if world.lower() in name.lower():
                self.add_error("name", "Имя содержит запрещенные слова")
            elif world.lower() in description.lower():
                self.add_error("description", "Описание содержит запрещенные слова")
        return cleaned_data
