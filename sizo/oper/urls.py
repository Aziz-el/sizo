from django.contrib import admin
from django.urls import path
from .views import RegisterAPIView,UserViewSet
urlpatterns = [
    path('register/',RegisterAPIView.as_view()),
]