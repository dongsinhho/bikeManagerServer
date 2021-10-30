from .models import Edge 
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict

channel_layer = get_channel_layer()

@shared_task
def send_location():
    edge = Edge.objects.all()
    data = model_to_dict(edge)
                
    async_to_sync(channel_layer.group_send)('client', {'type': 'send_new_data', 'text': data})

