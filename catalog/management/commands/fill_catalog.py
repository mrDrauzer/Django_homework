from django.core.management.base import BaseCommand
from catalog.models import Category, Product, Contact


class Command(BaseCommand):
    help = 'Заполнение каталога тестовыми данными'

    def handle(self, *args, **options):
        # Удаление существующих данных
        self.stdout.write('Удаление существующих данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()

        # Создание категорий
        self.stdout.write('Создание категорий...')
        electronics = Category.objects.create(
            name='Электроника',
            description='Электронные товары'
        )

        clothing = Category.objects.create(
            name='Одежда',
            description='Одежда и аксессуары'
        )

        books = Category.objects.create(
            name='Книги',
            description='Художественная и техническая литература'
        )

        # Создание продуктов
        self.stdout.write('Создание продуктов...')
        Product.objects.create(
            name='iPhone 15',
            description='Современный смартфон Apple',
            price=99999.99,
            category=electronics
        )

        Product.objects.create(
            name='Samsung Galaxy S24',
            description='Флагманский Android смартфон',
            price=89999.99,
            category=electronics
        )

        Product.objects.create(
            name='Куртка зимняя',
            description='Теплая зимняя куртка',
            price=15000.00,
            category=clothing
        )

        Product.objects.create(
            name='Джинсы',
            description='Стильные джинсы',
            price=8000.00,
            category=clothing
        )

        Product.objects.create(
            name='Python для начинающих',
            description='Учебник по программированию',
            price=2500.00,
            category=books
        )

        # Создание контактов
        self.stdout.write('Создание контактов...')
        Contact.objects.create(
            name='SkyStore',
            email='info@skystore.ru',
            phone='+7 (495) 123-45-67',
            address='г. Москва, ул. Примерная, д. 1'
        )

        self.stdout.write(
            self.style.SUCCESS('Каталог успешно заполнен тестовыми данными!')
        )

        # Статистика
        self.stdout.write(f'Создано категорий: {Category.objects.count()}')
        self.stdout.write(f'Создано продуктов: {Product.objects.count()}')
        self.stdout.write(f'Создано контактов: {Contact.objects.count()}')
