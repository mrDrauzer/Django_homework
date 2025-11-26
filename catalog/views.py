from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_moderator'] = user.is_authenticated and user.groups.filter(name='Модератор продуктов').exists()
        context['can_unpublish'] = user.is_authenticated and user.has_perm('catalog.can_unpublish_product')
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание нового товара"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Назначение владельца товара"""
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование товара — только для владельца или модератора"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        """После редактирования — на страницу товара"""
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        user = request.user
        is_moderator = user.groups.filter(name="Модератор продуктов").exists()
        has_perm = user.has_perm('catalog.can_unpublish_product')
        if obj.owner == user or is_moderator or has_perm:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Нет доступа к изменению!")

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление товара — только для владельца или модератора"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        user = request.user
        is_moderator = user.groups.filter(name="Модератор продуктов").exists()
        has_perm = user.has_perm('catalog.can_unpublish_product')
        if obj.owner == user or is_moderator or has_perm:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Нет доступа к удалению!")

class ContactsView(TemplateView):
    """Страница контактов"""
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
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
