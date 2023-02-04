from django.contrib import admin
from django.urls import path, include,re_path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    LogoutView,
)

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

API_TITLE = "Blog API"
API_DESCRIPTION = "This document describes how to use my own blog page for their frontend"

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('facebook.urls')),
    path('authenticate/', include('authentication.urls')),
    path('password-reset-view/', PasswordResetView.as_view(), name='password_reset_view'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api/v1/', include('api.urls')),
    path('auth-api/', include('rest_framework.urls')),
    # re_path(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    # re_path(r'^api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger-docs/', schema_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
