from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    create = models.DateTimeField(auto_created=True, auto_now=True)


class Edge(models.Model):
    latitude = models.DecimalField(max_digits=10,decimal_places=6)
    longtitude = models.DecimalField(max_digits=10,decimal_places=6)    
    mode = models.BooleanField() # True: được thuê, flase: đang rảnh


class bill(models.Model):
    timeStart = models.DateTimeField(auto_now=False, auto_now_add=False)
    timeFinish = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.BooleanField(default=False) # True: đã trả, False: chưa trả
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    edge = models.ForeignKey(Edge,on_delete=models.CASCADE)