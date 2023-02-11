from django.urls import path

from . import views

urlpatterns = [
    path('get_teams/', views.get_teams),
    path('create_team/', views.create_team),
    path('get_team/<uuid:team_id>/', views.get_team),
]