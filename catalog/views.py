from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Contact


def home(request):
    """Контроллер главной страницы"""
    latest_products = Product.objects.order_by('-created_at')[:5]

    context = {
        'latest_products': latest_products,
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Контроллер страницы контактов"""
    context = {}

    if request.method == 'POST':
        # Обработка формы обратной связи
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        context['message_sent'] = True

    # Получаем контактные данные из БД
    context['contact_info'] = Contact.objects.first()

    return render(request, 'catalog/contacts.html', context)


def product_list(request):
    """Контроллер списка продуктов"""
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog/product_list.html', context)


def category_products(request, category_id):
    """Контроллер продуктов определенной категории"""
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'catalog/category_products.html', context)
