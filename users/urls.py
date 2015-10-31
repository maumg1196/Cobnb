from django.conf.urls import include, url

urlpatterns = [

    url(r'^signin/$', 'users.views.signin_view', name='signin'),
    url(r'^signup/$', 'users.views.signup_view', name='signup'),
    url(r'^logout/$', 'users.views.logout_view', name='logout'),

]
