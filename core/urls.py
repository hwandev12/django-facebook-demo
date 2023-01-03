from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('facebook.urls')),
    path('authenticate/', include('authentication.urls')),
]
