from django.conf.urls import include, url

urlpatterns = [

    url(r'^$',
        'places.views.home',
        name='home'),

    url(r'^create_place/$',
        'places.views.new_place',
        name='new_place'),

]
