"""
ASGI config for resume_builder project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_builder.settings')

application = get_asgi_application()
