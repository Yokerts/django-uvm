"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.contrib.auth import get_user_model

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

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