from django.conf.urls import url

from . import views

from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^index', views.index, name='base.html'),
    url(r'^search/(?P<isci>\w+?)$', views.search_results, name='iskanje'),
    url(r'^clani', views.clani, name='clani'),
    url(r'^profil/(?P<clan_id>[0-9]+)$', views.get_name , name='profil'),
    url(r'^dodaj', views.dodajClan , name='dodaj'),

    url(r'^', auth_views.login, {'template_name': 'taborniki/login.html'} , name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

    ]