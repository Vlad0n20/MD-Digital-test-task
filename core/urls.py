from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('apps.user.urls', namespace='user'), name='user'),
    path('api/v1/', include('apps.group.urls', namespace='team'), name='team'),
]

urlpatterns += doc_urls
