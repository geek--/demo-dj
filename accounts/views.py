"""Views for user registration and authentication."""

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View

from .forms import StyledAuthenticationForm, UserRegistrationForm


class UserLoginView(LoginView):
    """Render the login form."""

    template_name = "registration/login.html"
    redirect_authenticated_user = True
    form_class = StyledAuthenticationForm


class UserLogoutView(View):
    """Render a custom logged-out screen and clear the session."""

    template_name = "registration/logged_out.html"
    http_method_names = ["get", "post", "head", "options"]

    def _logout_and_render(self, request: HttpRequest) -> HttpResponse:
        was_authenticated = request.user.is_authenticated
        logout(request)
        if was_authenticated:
            messages.success(request, "Has cerrado sesión correctamente.")
        return render(request, self.template_name)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return self._logout_and_render(request)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return self._logout_and_render(request)


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
