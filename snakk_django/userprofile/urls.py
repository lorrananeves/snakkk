from django.urls import path

from . import views

urlpatterns = [
    path('get_my_information/', views.get_my_information),
]