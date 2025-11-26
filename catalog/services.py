from django.conf import settings
from django.core.cache import cache
from catalog.models import Product

def get_products_by_category(category_pk):
    """Возвращает список продуктов по категории с кешированием."""
    if not settings.CACHE_ENABLED:
        return Product.objects.filter(category_id=category_pk)

    key = f'products_category_{category_pk}'
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.filter(category_id=category_pk)
    cache.set(key, products, 60 * 15)
    return products