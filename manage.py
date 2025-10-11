#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def print_server_info():
    """Вывод информации о доступных URL при запуске runserver"""
    if len(sys.argv) >= 2 and sys.argv[1] == 'runserver':
        port = "8000"  # Порт по умолчанию

        # Проверяем, указан ли другой порт
        for arg in sys.argv[2:]:
            if arg.isdigit() or ':' in arg:
                if ':' in arg:
                    port = arg.split(':')[1]
                else:
                    port = arg
                break

        print("\n" + "=" * 70)
        print("🚀 Запуск Django Development Server")
        print("=" * 70)
        print("\n📍 Доступные URL-адреса:")
        print(f"   • Главная страница:     http://127.0.0.1:{port}/")
        print(f"   • Блог:                 http://127.0.0.1:{port}/blog/")
        print(f"   • Админ-панель:         http://127.0.0.1:{port}/admin/")
        print(f"   • Контакты:             http://127.0.0.1:{port}/contacts/")
        print("\n💡 Для остановки сервера нажмите CTRL+C")
        print("=" * 70 + "\n")


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skystore.settings")

    # Выводим информацию перед запуском runserver
    print_server_info()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
