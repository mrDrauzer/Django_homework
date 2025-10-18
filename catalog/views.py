from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product
from .forms import ProductForm  # ✅ Импортируем форму


class ProductListView(ListView):
    """Список товаров на главной странице"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    """Детальная страница товара"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    """Создание нового товара"""
    model = Product
    form_class = ProductForm  # ✅ Используем форму вместо fields
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    """Редактирование товара"""
    model = Product
    form_class = ProductForm  # ✅ Используем форму вместо fields
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        """Перенаправляем на страницу товара после редактирования"""
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    """Удаление товара"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'  # ✅ Добавляем шаблон
    success_url = reverse_lazy('catalog:home')


class ContactsView(TemplateView):
    """Страница контактов"""
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        """Обработка отправки формы контактов"""
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Получено сообщение от {name} ({email}): {message}')
        return self.render_to_response(self.get_context_data())
