from __future__ import annotations

import sys
import uuid
from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.conf import settings


class Command(BaseCommand):
    help = (
        "Проверка доступности текущего бэкенда кэша. "
        "Выполняет тестовую операцию set/get. Если используется Redis и он не запущен — будет ошибка."
    )

    def handle(self, *args, **options):
        backend = cache.__class__.__module__ + "." + cache.__class__.__name__
        location = None

        # Попробуем вытащить LOCATION из настроек для наглядности
        try:
            location = settings.CACHES.get("default", {}).get("LOCATION")
        except Exception:
            location = None

        self.stdout.write(self.style.NOTICE(f"Бэкенд кэша: {backend}"))
        if location:
            self.stdout.write(self.style.NOTICE(f"LOCATION: {location}"))

        # Тестовая запись/чтение
        test_key = f"cache_ping:{uuid.uuid4()}"
        test_val = str(uuid.uuid4())
        try:
            cache.set(test_key, test_val, timeout=10)
            read_val = cache.get(test_key)
            if read_val == test_val:
                self.stdout.write(self.style.SUCCESS("Кэш доступен: set/get работает"))
                # Удалим ключ за собой
                cache.delete(test_key)
                return
            else:
                self.stdout.write(self.style.WARNING("Кэш ответил, но значение не совпало"))
                sys.exit(2)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при обращении к кэшу: {e}"))
            # Ненулевой код возврата удобен для CI/скриптов
            sys.exit(1)
