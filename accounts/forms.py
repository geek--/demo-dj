"""Forms for the accounts app."""

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """Extend the default user creation form to include email."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True


class StyledAuthenticationForm(AuthenticationForm):
    """Authentication form with placeholders and consistent styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"placeholder": "Ingrese su correo corporativo", "autofocus": True}
        )
        self.fields["password"].widget.attrs.update(
            {"placeholder": "Ingrese su contraseña"}
        )
