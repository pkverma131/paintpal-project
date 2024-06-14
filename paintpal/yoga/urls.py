from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YogaPathViewSet, YogasanaViewSet

router = DefaultRouter()
router.register(r'yoga-paths', YogaPathViewSet)
router.register(r'yogasanas', YogasanaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
