from django.urls import path
from . import views

urlpatterns = [
    path('bikes/<int:pk>/', views.BikeInfoView.as_view()),
    path("users/login/", views.UserLoginView.as_view()),
    path("users/register/", views.UserRegisterView.as_view(),name='register'),
    path("users/<int:pk>", views.UserDetail.as_view()),
    
    
]