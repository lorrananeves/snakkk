from django.urls import path

from .views import new_channel

urlpatterns = [
    path('new_channel/', new_channel),
]