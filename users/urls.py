from django.urls import path
from . import views

urlpatterns = [
    path('api/signup/', views.UserCreateAPIView),

    ]