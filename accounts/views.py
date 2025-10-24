"""Views for user registration and authentication."""

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from .forms import UserRegistrationForm


class UserLoginView(LoginView):
    """Render the login form."""

    template_name = "registration/login.html"
    redirect_authenticated_user = True


class RegisterView(View):
    """Allow users to create an account."""

    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("home")

    def get(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Tu cuenta ha sido creada correctamente.")
            return redirect(self.success_url)

        return render(request, self.template_name, {"form": form})
