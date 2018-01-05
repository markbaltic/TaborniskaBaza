# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import chain

from django.shortcuts import render, redirect
import django.contrib.postgres.search as search
from django.http import HttpResponse
from taborniki.models import Oseba, Vod, Rod
from django.db.models import Q
from .forms import NameForm, DodajClan, Search


def search_results(request):
    form = Search(request.GET)
    if form.is_valid():
        isci = form.cleaned_data['q']
        # poiščemo po imenu
        clani1 = Oseba.objects.filter(ime__contains=isci)
        # poiščemo po priimku
        clani2 = Oseba.objects.filter(priimek__contains=isci)
        # združimo in odstranimo duplikate
        clani = list(set(list(chain(clani1, clani2))))
        # najdemo vode
        vodi = list(Vod.objects.filter(imeVod__contains = isci))
        #najdemo rode
        rodi = list(Rod.objects.filter(imeRod__contains=isci))
        if clani or vodi or rodi:
            return render(request, 'taborniki/tabele.html', {'clani': clani, 'vodi':vodi, 'rodi' : rodi})
        else:
            return render(request, 'taborniki/no_results.html', {'isci': isci})
    else:
        redirect('/taborniki/index')







def index(request):
    form = Search()
    return render(request,'taborniki/base.html',  {'form': form} )

def login(request):
    return render(request,'taborniki/login.html' )

def profil(request):
    return render(request,'taborniki/search_results.html')

def clani(request):
    clani = Oseba.objects.all()
    output = ', '.join([p.__str__() for p in clani])
    return HttpResponse(output)

def get_name(request, clan_id):
    clan = Oseba.objects.get(id = clan_id)
    return render(request, 'taborniki/search_results.html', {'clan': clan})

def get_vod(request, vod_id):
    vod = Vod.objects.get(id = vod_id)

    return render(request, 'taborniki/vod.html', {'vod': vod})

def get_rod(request, rod_id):
    rod = Rod.objects.get(id = rod_id)
    return render(request, 'taborniki/rod.html', {'rod': rod})
def dodajClan(request):
    if request.method == 'POST':
        form = DodajClan(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            clan = Oseba.objects.create(ime = data['ime'],priimek=data['priimek'], naslov=data['naslov'],
                                        telefon=data['telefon'] , email=data['email'] , rojstvo=data['rojstvo']  )
            clan.save()

            return redirect('/taborniki/profil/%s' % clan.id )


    # if a GET (or any other method) we'll create a blank form
    else:
        form = DodajClan()

    return render(request, 'taborniki/dodajClan.html', {'form': form})