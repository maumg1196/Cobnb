from django.conf.urls import include, url
from django.contrib import admin
from cobnb import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/$', 'users.views.signin_view'),
    url(r'^signup/$', 'users.views.signup_view'),
]
