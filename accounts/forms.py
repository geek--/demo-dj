"""Forms for the accounts app."""

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """Extend the default user creation form to include email and styling."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

        field_placeholders = {
            "username": "Ej. agricultor.natu",
            "email": "correo@natuseeds.com",
            "password1": "Contraseña segura",
            "password2": "Repite tu contraseña",
        }

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "placeholder": field_placeholders.get(name, ""),
                    "class": "auth-input",
                }
            )


class StyledAuthenticationForm(AuthenticationForm):
    """Authentication form with placeholders and consistent styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "Ingresa tu correo corporativo",
                "autofocus": True,
                "class": "auth-input",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "placeholder": "Ingresa tu contraseña",
                "class": "auth-input",
            }
        )
