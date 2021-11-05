from django.contrib import admin
from .models import Edge, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Edge)

#admin.site.register(User)
admin.site.register(User, UserAdmin)