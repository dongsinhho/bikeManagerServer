from .models import Edge, Bike
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .utils import Red
from django.core.exceptions import ObjectDoesNotExist

import json
from decimal import Decimal

def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

channel_layer = get_channel_layer()


@shared_task
def send_location():
    data = []
    for item in Red.getAllKey():
        if item.isnumeric():
            edge = Red.get(item)
            edge = json.loads(edge)
            edge['id'] = item
            # edge = json.dumps(edge, indent=4)
            print(edge)
            data.append(edge)
    data = json.dumps(data, default=default)

    async_to_sync(channel_layer.group_send)('client', {'type': 'send_new_data', 'text': data })

@shared_task
def replicate_redis():
    for item in Red.getAllKey():
        if item.isnumeric():
            try:
                edge = Edge.objects.get(id=int(item))
                data = Red.get(item)
                data = json.loads(data)
                bike = Bike(edge=edge,latitude=float(data["latitude"]), longtitude = float(data["longtitude"]))
                bike.save()
            except ObjectDoesNotExist:
                print("edge not exist")

