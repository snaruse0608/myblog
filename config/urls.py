from django.contrib import admin
from django.urls import path, include
from . import settings_common
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('myblog.urls')),
    path('markdownx/', include('markdownx.urls')),
]

urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_common.MEDIA_ROOT)