from django.urls import path, include
from rest_framework import routers
from .views import TrackViewSet


router = routers.DefaultRouter()
router.register(prefix='tracks', viewset=TrackViewSet, basename='tracks')

urlpatterns = [
    path('', include(router.urls), name='track_api'),
]