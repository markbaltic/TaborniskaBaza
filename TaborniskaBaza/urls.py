"""TBaza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url, include
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
#
#
# admin.autodiscover()
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^taborniki/', include('taborniki.urls')),
#     url(r'^$', auth_views.login, {'template_name': 'taborniki/login.html'}, name='login'),
#
# ]

from django.conf.urls import url

from taborniki import views

from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^taborniki/index', views.index, name='index'),
    url(r'^taborniki/search', views.search_results, name='search'),

    url(r'^taborniki/clani', views.clani, name='clani'),
    url(r'^taborniki/vsiclani', views.vsi_clani, name='vsiClani'),
    url(r'^taborniki/vsivodi', views.vsi_vodi, name='vsiVodi'),
    url(r'^taborniki/odstraniclanavoda/(?P<clan_id>[0-9]+)$', views.odstrani_clana_voda, name='odstraniClanaVoda'),
    url(r'^taborniki/vseakcije', views.vse_akcije, name='vseAkcije'),
    url(r'^taborniki/profil/(?P<clan_id>[0-9]+)$', views.get_name , name='profil'),
    url(r'^taborniki/dodajAkcija', views.dodajAkcija , name='dodajAkcija'),
    url(r'^taborniki/dodaj', views.dodajClan , name='dodaj'),
    url(r'^taborniki/vod/(?P<vod_id>[0-9]+)$', views.get_vod , name='vod'),
    url(r'^taborniki/vod/dodaj/(?P<vod_id>[0-9]+)$', views.dodaj_clana_vodu , name='dodaj_clana_vodu'),
    url(r'^taborniki/rod/(?P<rod_id>[0-9]+)$', views.get_rod , name='rod'),
    url(r'^taborniki/profil/odstrani/(?P<clan_id>[0-9]+)$', views.odstrani_clan , name='odstraniClan'),
    url(r'^taborniki/akcija/(?P<akcija_id>[0-9]+)$', views.get_akcija , name='akcija'),
    url(r'^taborniki/akcija/dodaj/(?P<akcija_id>[0-9]+)$', views.dodaj_clana_akciji , name='dodaj_clana_akciji'),
    url(r'^taborniki/$', auth_views.login, {'template_name': 'taborniki/login.html'} , name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls)

]