"""Utility helpers for settings modules."""

from __future__ import annotations

import os
from pathlib import Path


def load_env_file(path: str | os.PathLike[str]) -> None:
    """Populate ``os.environ`` with variables declared in ``path``.

    The loader understands simple ``KEY=VALUE`` pairs and ignores blank lines
    and comments starting with ``#``. Existing environment variables take
    precedence and will not be overwritten.
    """

    env_path = Path(path)

    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())
