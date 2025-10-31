from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, UserLoginForm
from .models import User


class RegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'  # ✅ Изменил путь!
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Обработка валидной формы"""
        # Сохраняем пользователя
        user = form.save()

        # Автоматически входим после регистрации
        login(self.request, user)

        # Отправляем приветственное письмо
        send_mail(
            subject='Добро пожаловать в SkyStore!',
            message=f'Здравствуйте, {user.email}!\n\nСпасибо за регистрацию в нашем интернет-магазине.',
            from_email=None,  # Будет использован DEFAULT_FROM_EMAIL из settings
            recipient_list=[user.email],
            fail_silently=False,
        )

        return super().form_valid(form)


class UserLoginView(LoginView):
    """Авторизация пользователя"""
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        """URL для редиректа после успешного входа"""
        return reverse_lazy('catalog:home')


class UserLogoutView(LogoutView):
    """Выход пользователя"""
    next_page = reverse_lazy('catalog:home')
