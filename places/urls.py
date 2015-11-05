from django.conf.urls import include, url
from places.views import HomeView, CreatePlace

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^place_form/$',
        CreatePlace.as_view(),
        name='new_place'),

]
