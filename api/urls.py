from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    PostAPIView,
    UserList,
)

router = SimpleRouter()
router.register('users', UserList, basename='users')
router.register('', PostAPIView, basename='posts')

urlpatterns = router.urls