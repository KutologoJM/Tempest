# settings/local.py
from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
INTERNAL_IPS = [
    "127.0.0.1",
]


INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(2, "debug_toolbar.middleware.DebugToolbarMiddleware")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',
    'imgur': 'true',
    'mention': 'true',
    'jquery': 'true',
    'living': 'true',     # Enable for immediate feedback
    'spellcheck': 'true', # Enable for writing assistance
    'hljs': 'true',
}

MARTOR_MARKDOWNIFY_TIMEOUT = 0  # Instant updates