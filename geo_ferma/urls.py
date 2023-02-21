from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/post/', include(('app.urls', 'app'), namespace='app')),
                  path('api/v1/rest-auth/', include('rest_auth.urls')),
                  path('api/v1/rest-auth/register/', include('rest_auth.registration.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
