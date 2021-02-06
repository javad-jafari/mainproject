from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse
from django.views import View
from django.views.generic import RedirectView, DetailView

from Accounts.forms import UserThirdRegistrationForm
from Products.models import Category

User = get_user_model()


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SignView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class RegisterView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'registration/register.html', {'form': UserThirdRegistrationForm})

    def post(self, request):
        form = UserThirdRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse('userprofile'))

        return render(request, 'registration/register.html', {'form': form})


class UserProfileView(DetailView, LoginRequiredMixin):
    model = User
    login_url = '/'
    redirect_field_name = 'home'
    template_name = 'registration/user_profile.html'
    pk_url_kwarg = 'user_id'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
