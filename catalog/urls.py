from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ContactsView,
    CategoryProductListView
)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    # Добавляем категорию
    path('category/<int:pk>/', CategoryProductListView.as_view(), name='category_products'),

    # CRUD
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    # Добавляем cache_page
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]