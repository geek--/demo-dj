"""Development settings."""

from pathlib import Path

from .utils import load_env_file

load_env_file(Path(__file__).resolve().parent.parent.parent / "envs" / "dev.env")

from .base import *  # noqa: F401,F403

DEBUG = True

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
