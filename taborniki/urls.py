from django.conf.urls import url

from . import views

from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [


    url(r'^search', views.search_results, name='search'),
    url(r'^clani', views.clani, name='clani'),
    url(r'^profil/(?P<clan_id>[0-9]+)$', views.get_name , name='profil'),
    url(r'^dodaj', views.dodajClan , name='dodaj'),
    url(r'^vod/(?P<vod_id>[0-9]+)$', views.get_vod , name='vod'),
    url(r'^[a-zA-Z]', views.index, name='index'),

    url(r'^', auth_views.login, {'template_name': 'taborniki/login.html'} , name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

    ]