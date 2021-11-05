from .models import Edge 
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

import json
from decimal import Decimal

def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

channel_layer = get_channel_layer()


@shared_task
def send_location():
    edges = Edge.objects.all()
    data = []
    for edge in edges:
        edge = model_to_dict(edge)
        data.append(edge)
    result = json.dumps(data, default=default)
    async_to_sync(channel_layer.group_send)('client', {'type': 'send_new_data', 'text': result})

