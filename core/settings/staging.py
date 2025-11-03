"""Staging settings."""

from pathlib import Path

from .utils import load_env_file

load_env_file(Path(__file__).resolve().parent.parent.parent / "envs" / "staging.env")

from .base import *  # noqa: F401,F403

import os

DEBUG = False

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split() or ["staging.example.com"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
