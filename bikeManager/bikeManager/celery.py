import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','bikeManager.settings')

app = Celery('bikeManager')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send_location_edge_inRedis': {
        'task': 'api.tasks.send_location',
        'schedule': 5.0
    },
    'replicate_data_location': {
        'task': 'api.tasks.replicate_redis',
        'schedule': 20.0
    }
}

app.autodiscover_tasks()