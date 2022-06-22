
import os
from celery import Celery
from backend import settings
import os
from celery import Celery

def bootstrap_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    import django

    django.setup()

bootstrap_django()

from api.models import *

def build_app():
    redis = "redis://:{0}@{1}:{2}".format(
        settings.REDIS["default"]["PASSWORD"],
        settings.REDIS["default"]["HOST"],
        settings.REDIS["default"]["PORT"]
    )
    return Celery("tasks", backend=redis, broker=redis)


app = build_app()



@app.task(bind=True)
def celery_task(self, config):
    pass