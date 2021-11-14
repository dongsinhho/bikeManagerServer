from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('bikes/<int:pk>/', BikeInfoView.as_view()),
    path("users/login/", UserLoginView.as_view()),
    path("users/register/", UserRegisterView.as_view(),name='register'),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("bills/", BillView.as_view()),
    path("bills/<int:pk>/", BillDetailView.as_view())
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)