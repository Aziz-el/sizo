from .views import CreateCategory
from django.urls import path
urlpatterns = [
    path("create",CreateCategory.as_view()),
]