from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')


class HomePageView(TemplateView):
    template_name = 'home.html'


class ProtectedPageView(LoginRequiredMixin, TemplateView):
    template_name = 'page.html'
    login_url = reverse_lazy('login')
