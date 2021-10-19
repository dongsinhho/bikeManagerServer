from django.urls import path
from . import views

urlpatterns = [
    path('bike/', views.EdgeInfo.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>", views.UserDetail.as_view()),
]