# Demo Django

Proyecto base de Django configurado para múltiples entornos y preparado para vistas web tradicionales y APIs.

## Características

- Configuración separada para `development`, `staging` y `production`.
- Base de datos PostgreSQL configurable mediante variables de entorno.
- Frontend basado en plantillas de Django con vistas de inicio de sesión y registro.
- Preparado para exponer APIs mediante Django REST Framework.

## Requisitos

- Python 3.11+
- Dependencias indicadas en `requirements.txt`
- Base de datos PostgreSQL disponible

## Configuración rápida

1. Crea un entorno virtual e instala dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Define las variables de entorno necesarias:
   ```bash
   export DJANGO_SETTINGS_MODULE=core.settings.development
   export POSTGRES_DB=demo_dj
   export POSTGRES_USER=demo_dj
   export POSTGRES_PASSWORD=demo_dj
   export POSTGRES_HOST=localhost
   export POSTGRES_PORT=5432
   ```
3. Ejecuta las migraciones y levanta el servidor de desarrollo:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Las vistas de autenticación están disponibles en `/accounts/login/` y `/accounts/register/`.
