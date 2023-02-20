from django.urls import path

from . import views

urlpatterns = [
    path('get_messages/<uuid:team_id>/', views.get_messages),
]