from django.urls import path

from . import views

urlpatterns = [
    path('get_teams/', views.get_teams),
    path('create_team/', views.create_team),
]