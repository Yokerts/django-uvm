#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.contrib.auth import get_user_model

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


if os.environ.get("CREATE_SUPERUSER", "false").lower() == "true":
    try:
        User = get_user_model()
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "yokerts1689@live.com.mx")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin1616")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"✅ Superusuario '{username}' creado automáticamente.")
        else:
            print(f"ℹ️ El superusuario '{username}' ya existe, no se creó de nuevo.")
    except Exception as e:
        print(f"⚠️ Error al crear superusuario: {e}")