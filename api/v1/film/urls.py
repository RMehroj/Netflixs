
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from . import views

from .views import (
    MovieViewSet,
    ActorVievSet,
    )

router = DefaultRouter()

router.register('movies', MovieViewSet)
router.register('actors', ActorVievSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]