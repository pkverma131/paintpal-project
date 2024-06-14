from django.urls import path, include
from .api import api_router#, router

urlpatterns = [
    path('api/v2/', api_router.urls),
    # path('api/v1/', include(router.urls)),
]