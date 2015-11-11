from django.conf.urls import include, url
from places.views import ListPlace, CreatePlace, PlaceDetail

urlpatterns = [

    url(r'^list_place/',
        ListPlace.as_view(),
        name='home'),

    url(r'^create_place/$',
        CreatePlace.as_view(),
        name='new_place'),

    url(r'^place_detail/(?P<pk>[0-9]+)',
        PlaceDetail.as_view(),
        name='place_detail'),

]
