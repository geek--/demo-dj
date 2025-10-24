"""URL configuration for the project."""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from accounts.views import UserLoginView, UserLogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", UserLoginView.as_view(), name="login"),
    path("accounts/logout/", UserLogoutView.as_view(), name="logout"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
]
