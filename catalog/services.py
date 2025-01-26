from .models import Product
from django.core.cache import cache
from config.settings import CACHE_ENABLED


def get_product_from_cache_or_db(category):
    if CACHE_ENABLED:
        key = "queryset_category"
        queryset_category = cache.get(key)
        if not queryset_category:
            queryset_category = Product.objects.filter(category=category)
            cache.set(key, queryset_category, 60 * 15)
        return queryset_category
    queryset_category = Product.objects.filter(category=category)
    return queryset_category
