from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index.html'),
    url(r'^clani', views.clani, name='clani'),
    url(r'^profil', views.get_name , name='profil'),
    url(r'^dodaj', views.dodajClan , name='dodaj'),
    ]