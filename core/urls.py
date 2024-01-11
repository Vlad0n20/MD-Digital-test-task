from django.contrib import admin
from django.urls import path, include

from core.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.user.urls', namespace='user'), name='user'),
]

urlpatterns += doc_urls
