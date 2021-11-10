from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=255)
    avatar = models.URLField(max_length=255, default="")
    balance = models.IntegerField(default=0)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    create = models.DateTimeField(auto_created=True, auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    def __str__(self):
        return self.username


class Edge(models.Model):
    latitude = models.DecimalField(max_digits=10,decimal_places=6)
    longtitude = models.DecimalField(max_digits=10,decimal_places=6)    
    mode = models.BooleanField(default=False) # True: được thuê, false: đang rảnh
    def __str__(self):
        return str(self.pk)

class Bill(models.Model):
    timeStart = models.DateTimeField(auto_now=False,auto_now_add=False)
    timeFinish = models.DateTimeField(auto_now=False, auto_now_add=False, default=None, null=True, blank=True)
    status = models.BooleanField(default=False) # True: đã trả, False: chưa trả
    cost = models.IntegerField(default=100)
    user = models.ForeignKey(User,related_name='Bills',on_delete=models.CASCADE)
    edge = models.ForeignKey(Edge,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)