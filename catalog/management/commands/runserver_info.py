from django.core.management.commands.runserver import Command as RunserverCommand


class Command(RunserverCommand):
    help = 'Запуск сервера разработки с дополнительной информацией'

    def handle(self, *args, **options):
        """Переопределяем метод запуска сервера"""

        # Получаем порт (по умолчанию 8000)
        addrport = options.get('addrport') or '8000'
        if ':' in addrport:
            port = addrport.split(':')[1]
        else:
            port = addrport

        # Выводим красивую информацию
        self.stdout.write("\n" + "=" * 70)
        self.stdout.write(self.style.SUCCESS("🚀 Запуск Django Development Server"))
        self.stdout.write("=" * 70 + "\n")

        self.stdout.write("📍 Доступные URL-адреса:\n")
        self.stdout.write(f"   • Главная страница:     http://127.0.0.1:{port}/")
        self.stdout.write(f"   • Блог:                 http://127.0.0.1:{port}/blog/")
        self.stdout.write(f"   • Админ-панель:         http://127.0.0.1:{port}/admin/")
        self.stdout.write(f"   • Контакты:             http://127.0.0.1:{port}/contacts/")

        self.stdout.write("\n💡 Для остановки сервера нажмите CTRL+C")
        self.stdout.write("=" * 70 + "\n\n")

        # Запускаем обычный runserver
        super().handle(*args, **options)
