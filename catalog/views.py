from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm
from catalog.models import Category
from catalog.services import get_products_by_category


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание нового товара"""
    model = Product
    form_class = ProductForm  # ✅ Используем форму вместо fields
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование товара"""
    model = Product
    form_class = ProductForm  # ✅ Используем форму вместо fields
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        """Перенаправляем на страницу товара после редактирования"""
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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

class CategoryProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return get_products_by_category(category_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_pk = self.kwargs['pk']
        category = Category.objects.get(pk=category_pk)
        context['title'] = category.name
        return context
