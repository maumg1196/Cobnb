from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from cobnb import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('users.urls', namespace='users')),
    url('', include('places.urls', namespace='places')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
