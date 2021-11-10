from django.urls import path
from .views import *

urlpatterns = [
    path('bikes/<int:pk>/', BikeInfoView.as_view()),
    path("users/login/", UserLoginView.as_view()),
    path("users/register/", UserRegisterView.as_view(),name='register'),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("bills/", BillView.as_view()),
    path("bills/<int:pk>/", BillDetailView.as_view())
]