"""
WSGI config for scrapd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv(verbose=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapd.settings')

application = get_wsgi_application()