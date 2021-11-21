from django.contrib import admin
from .models import Edge, User, Bill, Bike
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Edge)
admin.site.register(Bill)
admin.site.register(Bike)
admin.site.register(User, UserAdmin)