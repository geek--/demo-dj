"""Production settings."""

from pathlib import Path

from .utils import load_env_file

load_env_file(Path(__file__).resolve().parent.parent.parent / "envs" / "prod.env")

from .base import *  # noqa: F401,F403

import os

DEBUG = False

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split() or ["example.com"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
