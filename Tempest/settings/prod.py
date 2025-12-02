# settings/production.py
from .base import *

DEBUG = False

ALLOWED_HOSTS = ["jezrastudio.online"]

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',
    'imgur': 'true',
    'mention': 'false',   # Disable if not needed
    'jquery': 'true',
    'living': 'false',    # Disable for better performance
    'spellcheck': 'false', # Let users handle this
    'hljs': 'true',
}

MARTOR_MARKDOWNIFY_TIMEOUT = 1000  # Reduce server load