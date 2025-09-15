from django.shortcuts import render


def home(request):
    """Контроллер главной страницы"""
    return render(request, 'catalog/home.html')


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

    return render(request, 'catalog/contacts.html', context)
