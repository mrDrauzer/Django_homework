from django.shortcuts import render
from .models import Product, Category


def home(request):
    """Контроллер главной страницы"""
    # Дополнительное задание - последние 5 продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(f"- {product.name} ({product.created_at})")

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
        print(f"Получено сообщение от {name} ({phone}): {message}")
        context['message_sent'] = True

    # Дополнительное задание - контактные данные из БД
    # После создания модели Contact раскомментируйте:
    # from .models import Contact
    # context['contact_info'] = Contact.objects.first()

    return render(request, 'catalog/contacts.html', context)


def index(request):
    """Контроллер главной страницы (альтернативное название)"""
    # Если используете index вместо home
    return home(request)


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
    try:
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category)

        context = {
            'category': category,
            'products': products,
        }
        return render(request, 'catalog/category_products.html', context)
    except Category.DoesNotExist:
        return render(request, 'catalog/404.html', status=404)
