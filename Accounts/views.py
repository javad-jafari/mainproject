from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse
from django.views import View
from django.views.generic import RedirectView

from Accounts.forms import UserThirdRegistrationForm

User = get_user_model()


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SignView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = '/'



class RegisterView(View):
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
            return redirect(reverse('login'))

        return render(request, 'registration/register.html', {'form': form})