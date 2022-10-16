from django.urls import path
from .views import Me, Users

urlpatterns = [
    path("me", Me.as_view()),
    path("", Users.as_view()),
]
