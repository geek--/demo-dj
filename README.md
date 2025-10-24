# Demo Django

Proyecto base de Django configurado para múltiples entornos y preparado para vistas web tradicionales y APIs.

## Características

- Configuración separada para `development`, `staging` y `production`.
- Base de datos PostgreSQL configurable mediante variables de entorno.
- Archivos `.env` específicos por entorno en `envs/` cargados automáticamente
  por los módulos de configuración.
- Frontend basado en plantillas de Django con vistas de inicio de sesión y registro.
- Preparado para exponer APIs mediante Django REST Framework.

## Requisitos

- Python 3.11+
- Dependencias indicadas en `requirements.txt`
- Base de datos PostgreSQL disponible

## Configuración rápida
1. Pre Configuración:
   ```bash
   pyenv global 3.12.3
   python --v
   ```
2. Crea un entorno virtual e :
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instala dependencias
   ```bash
   pip install -r requirements.txt
   ```
4. Copia y ajusta los archivos de variables de entorno ubicados en `envs/`.
   Para desarrollo puedes partir de `envs/dev.env` y modificar los valores
   según tu entorno local.

5. Base de datos.
   ```bash
   sudo -u postgres psql

   CREATE DATABASE demo_dj_dev;
   CREATE USER demo_dj WITH PASSWORD 'demo_dj';
   GRANT ALL PRIVILEGES ON DATABASE demo_dj_dev TO demo_dj;
   GRANT ALL ON SCHEMA public TO demo_dj;
   ```
6. Dependencias pre migrate
   ```bash
   mkdir static
   ```
3. Ejecuta las migraciones y levanta el servidor de desarrollo indicando el
   módulo de configuración correspondiente:
   ```bash
   python manage.py makemigrations --settings=core.settings.development
   python manage.py migrate --settings=core.settings.development
   python manage.py runserver --settings=core.settings.development
   ```

Las vistas de autenticación están disponibles en `/accounts/login/` y `/accounts/register/`.
