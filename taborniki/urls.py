from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^index', views.index, name='index.html'),
    url(r'^clani', views.clani, name='clani'),
    url(r'^profil/(?P<clan_id>[0-9]+)/$', views.get_name , name='profil'),
    url(r'^dodaj', views.dodajClan , name='dodaj'),
    url(r'^$', views.login, name='login'),

    ]