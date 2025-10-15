from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django import forms
from .models import Product, Category, Contact


class ProductListView(ListView):
    """Список всех товаров"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 12


class ProductDetailView(DetailView):
    """Детальная страница товара"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductForm(forms.ModelForm):
    """Форма для создания/редактирования товара"""

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')


class ProductCreateView(CreateView):
    """Создание нового товара"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


# ✅ Переводим FBV contacts на CBV
class ContactsView(TemplateView):
    """Страница контактов с формой обратной связи"""
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем контактную информацию из БД
        context['contact_info'] = Contact.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        """Обработка формы обратной связи"""
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Здесь можно сохранить данные или отправить email
        print(f'{name} ({phone}): {message}')

        # Добавляем флаг успешной отправки
        context = self.get_context_data(**kwargs)
        context['message_sent'] = True
        return self.render_to_response(context)


# ✅ Переводим FBV category_products на CBV
class CategoryProductsView(ListView):
    """Список товаров в категории"""
    model = Product
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Фильтруем товары по категории"""
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = Category.objects.get(id=category_id)
        return context
