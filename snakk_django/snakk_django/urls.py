from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1', include('djoser.urls.authtoken')),
    path('api/v1/userprofile/', include('userprofile.urls')),
    path('api/v1/teams/', include('team.urls')),
]
