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
