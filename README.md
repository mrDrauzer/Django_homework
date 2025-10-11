# Django Homework - SkyStore

Интернет-магазин на Django с PostgreSQL

## 🚀 Что реализовано

### 📦 Домашнее задание #1
- ✅ **PostgreSQL подключение** - база данных настроена
- ✅ **3 модели**: Category, Product (с связью), Contact  
- ✅ **Админка настроена**:
  - Category: отображение id, name + поиск
  - Product: отображение id, name, price, category + фильтр + поиск
- ✅ **Django Shell** - создание, получение, обновление, удаление
- ✅ **Кастомная команда** `fill_catalog` - заполнение тестовыми данными
- ✅ **Миграции** применены

### 🎨 Домашнее задание #2
- ✅ **Шаблоны и динамика**:
  - Базовый шаблон `base.html` с централизованными стилями
  - Подшаблон меню `_menu.html` через `{% include %}`
  - Главная страница со списком товаров (ProductListView)
  - Страница одного товара с полной информацией (ProductDetailView)
  - Страница контактов с формой обратной связи
  - Обрезка описания до 100 символов через фильтр `truncatechars`
  - Корректный вывод изображений через MEDIA_URL
  - Навигация между страницами (главная ↔ товар)
- ⭐ **Дополнительные задания**:
  - Форма добавления товара (ProductCreateView + ModelForm)
  - Постраничный вывод товаров — пагинация по 12 штук

---

## 🛠 Запуск проекта
1. Скопировать и настроить переменные окружения
cp .env.sample .env
Отредактируйте .env файл своими значениями
 
2. Применить миграции
python manage.py migrate

## 📋 Модели

### 🗂 Category (Категория)
name (CharField) — Наименование категории

description (TextField) — Описание категории


### 📦 Product (Продукт)
name (CharField) — Наименование продукта

description (TextField) — Описание продукта

image (ImageField) — Изображение продукта

category (ForeignKey) — Связь с категорией

price (DecimalField) — Цена за покупку

created_at (DateTimeField) — Дата создания (auto_now_add)

updated_at (DateTimeField) — Дата последнего изменения (auto_now)


### 📞 Contact (Контакт)
country (CharField) — Страна

inn (CharField) — ИНН организации

address (TextField) — Адрес


---

## 🎯 Админ-панель

**Доступ:** http://127.0.0.1:8000/admin/

### Функциональность:
- **Категории (Category)**:
  - Отображение: ID, название
  - Поиск по названию
  
- **Продукты (Product)**:
  - Отображение: ID, название, цена, категория
  - Фильтр по категории
  - Поиск по названию и описанию
  
- **Контакты (Contact)**:
  - Управление контактной информацией компании

---

## 🛠 Кастомные команды

### Заполнение каталога тестовыми данными
python manage.py fill_catalog


**Что делает команда:**
- Очищает существующие данные (Product, Category, Contact)
- Создаёт 2 категории: "Электроника" и "Одежда"
- Добавляет 5 тестовых товаров
- Создаёт контактную информацию

---

## 📁 Структура проекта
```
Django_homework/
├── manage.py
├── pyproject.toml
├── requirements.txt  
├── .env.sample
├── .gitignore
├── README.md
│
├── skystore/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── catalog/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── tests.py
│   │
│   ├── templates/
│   │   ├── catalog/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── product_detail.html
│   │   │   ├── product_form.html
│   │   │   └── contacts.html
│   │   └── includes/
│   │       └── _menu.html
│   │
│   ├── management/
│   │   ├── __init__.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── fill_catalog.py
│   │
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── media/
    └── products/
```



## 🔧 Технологии

| Технология | Версия | Описание |
|-----------|--------|----------|
| Python | 3.12 | Язык программирования |
| Django | 5.2.6 | Web-фреймворк |
| PostgreSQL | 15+ | База данных |
| Poetry | — | Управление зависимостями |
| python-decouple | — | Управление переменными окружения |
| Pillow | — | Обработка изображений |

---

## ✨ Особенности реализации

### 🎨 Шаблоны
- **Единый базовый шаблон** с централизованными стилями в `<style>` блоке
- **Подшаблон меню** через `{% include 'includes/_menu.html' %}`
- **Наследование** через `{% extends 'catalog/base.html' %}`
- **Блоки контента** для переопределения: `{% block content %}`

### 🔄 Views
- **Class-Based Views** для списков и деталей (ListView, DetailView)
- **ModelForm** для формы добавления товаров
- **Пагинация** через атрибут `paginate_by = 12`
- **Корректная обработка изображений** через ImageField + MEDIA_URL

### 🗺 URL Routing
- **Именованные маршруты** через атрибут `name` (например, `name='product_detail'`)
- **Правильная иерархия** через `include('catalog.urls')`
- **RESTful подход** к структуре URL
- **App namespace** через `app_name = 'catalog'`

### 🎯 Фильтры и теги шаблонов
- `truncatechars:100` — обрезка описания до 100 символов
- `{{ product.image.url }}` — корректный вывод изображений
- `{% url 'catalog:product_detail' product.pk %}` — безопасные ссылки

---

## ✅ Выполненные задания курса

### 📝 Домашнее задание #1:
1. ✅ Настройка подключения к PostgreSQL через python-decouple
2. ✅ Создание и регистрация моделей в админ-панели
3. ✅ Применение миграций (makemigrations + migrate)
4. ✅ Настройка отображения моделей в админке согласно требованиям
5. ✅ Работа с Django Shell (создание, чтение, обновление, удаление)
6. ✅ Создание фикстур с тестовыми данными
7. ✅ Написание кастомной команды управления `fill_catalog`

### 🎨 Домашнее задание #2:
1. ✅ Создание базового шаблона `base.html`
2. ✅ Создание подшаблона меню `_menu.html`
3. ✅ Реализация страницы одного товара (ProductDetailView с pk)
4. ✅ Главная страница со списком товаров (ProductListView)
5. ✅ Обрезка описания до 100 символов фильтром `truncatechars`
6. ✅ Навигация между страницами (главная ↔ товар)
7. ✅ Корректный вывод изображений через `product.image.url`
8. ⭐ Форма добавления товара (ProductCreateView + ModelForm)
9. ⭐ Постраничный вывод (пагинация через `paginate_by`)

---
