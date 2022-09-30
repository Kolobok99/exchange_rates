from django.contrib import admin
from django.urls import path, include

from apps.api import urls as api_urls
from .yasg import urlpatterns as docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
]

urlpatterns += docs_urls