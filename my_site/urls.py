from django.contrib import admin
from django.urls import path, include

from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
]

from django.conf.urls.static import static
from django.conf import settings#

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)