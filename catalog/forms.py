from django import forms
from django.core.exceptions import ValidationError
from .models import Product

# Константа с запрещёнными словами
FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования продукта"""

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название продукта'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Описание продукта',
                'rows': 5
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
        }

    def __init__(self, *args, **kwargs):
        """Стилизация формы через __init__"""
        super().__init__(*args, **kwargs)

        # Применяем стили ко всем полям
        for field_name, field in self.fields.items():
            # Для чекбокса (BooleanField) используем отдельный класс
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        """Валидация названия на запрещённые слова"""
        name = self.cleaned_data.get('name')

        if name:
            # Приводим к нижнему регистру для проверки
            name_lower = name.lower()

            # Проверяем наличие запрещённых слов
            for word in FORBIDDEN_WORDS:
                if word in name_lower:
                    raise ValidationError(
                        f'Название не может содержать запрещённое слово: "{word}"'
                    )

        return name

    def clean_description(self):
        """Валидация описания на запрещённые слова"""
        description = self.cleaned_data.get('description')

        if description:
            # Приводим к нижнему регистру для проверки
            description_lower = description.lower()

            # Проверяем наличие запрещённых слов
            for word in FORBIDDEN_WORDS:
                if word in description_lower:
                    raise ValidationError(
                        f'Описание не может содержать запрещённое слово: "{word}"'
                    )

        return description

    def clean_price(self):
        """Валидация цены - не может быть отрицательной"""
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise ValidationError(
                'Цена не может быть отрицательной'
            )

        return price

    def clean_image(self):
        """
        Валидируем изображение только если оно новое (загружается через форму)
        """
        image = self.cleaned_data.get('image')
        if image:
            # Только если это загруженный файл (InMemoryUploadedFile)
            content_type = getattr(image, 'content_type', None)
            if content_type:
                valid_formats = ['image/jpeg', 'image/png']
                if content_type not in valid_formats:
                    raise ValidationError(
                        'Загружайте изображения только в форматах JPEG или PNG'
                    )

                max_size = 5 * 1024 * 1024  # 5 МБ
                if image.size > max_size:
                    raise ValidationError(
                        f'Размер изображения не должен превышать 5 МБ. '
                        f'Текущий размер: {image.size / (1024 * 1024):.2f} МБ'
                    )
            # если image не имеет content_type — это просто "старый" файл, его не проверяем заново
        return image
