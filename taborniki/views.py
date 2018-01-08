# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import chain

from django.shortcuts import render, redirect
import django.contrib.postgres.search as search
from django.http import HttpResponse
from taborniki.models import Oseba, Vod, Rod, Akcija
from django.db.models import Q, Count
from .forms import NameForm, DodajClan, Search, DodajClanaVodu
import json


def search_results(request):
    form = Search(request.GET)
    if form.is_valid():
        isci = form.cleaned_data['q']
        # poiščemo po imenu
        clani = list(set(list(Oseba.objects.filter(Q(ime__icontains=isci) | Q(priimek__icontains=isci)))))

        # najdemo vode
        vodi = list(Vod.objects.filter(imeVod__icontains=isci))
        # najdemo rode
        rodi = list(Rod.objects.filter(imeRod__icontains=isci))
        # najdemo akcije
        print(isci)
        akcije = list(set(list(Akcija.objects.filter(imeAkcija__icontains=isci))))
        print(akcije)
        if clani or vodi or rodi or akcije:
            return render(request, 'taborniki/tabele.html',
                          {'clani': clani, 'vodi': vodi, 'rodi': rodi, 'akcije': akcije})
        else:
            return render(request, 'taborniki/no_results.html', {'isci': isci})
    else:
        redirect('/taborniki/index')


def index(request):
    form = Search()
    clan = Oseba.objects.get(id=6)

    rkjVodi = Vod.objects.all().filter(rod=1000).__len__()
    rorVodi = Vod.objects.all().filter(rod=1001).__len__()
    rcbVodi = Vod.objects.all().filter(rod=1002).__len__()
    rkjClani = Oseba.objects.all().filter(vod__rod=1000).__len__()
    rorClani = Oseba.objects.all().filter(vod__rod=1001).__len__()
    rcbClani = Oseba.objects.all().filter(vod__rod=1002).__len__()

    # akcija z največ udeleženci
    akcijaNAJ = Akcija.objects.all().values('imeAkcija').annotate(total=Count('udelezenci')).order_by('-total')[0][
        'imeAkcija']
    akcija = Akcija.objects.get(imeAkcija=akcijaNAJ)

    # udeleženec največ akcij
    # clanNAJ = Oseba.objects.all().values('akcija__udelezenci').annotate(total=Count('udelezenci')).order_by('-total')
    # print(clanNAJ)
    return render(request, 'taborniki/home.html',
                  {'form': form, 'ime': clan.ime, 'priimek': clan.priimek, 'rkjVodi': rkjVodi,
                   'rorVodi': rorVodi, 'rcbVodi': rcbVodi,
                   'rkjClani': rkjClani,
                   'rorClani': rorClani, 'rcbClani': rcbClani,
                   'akcija': akcija
                   })


def login(request):
    return render(request, 'taborniki/login.html')


def profil(request):
    return render(request, 'taborniki/search_results.html')


def clani(request):
    clani = Oseba.objects.all()
    output = ', '.join([p.__str__() for p in clani])
    return HttpResponse(output)


def get_name(request, clan_id):
    clan = Oseba.objects.get(id=clan_id)
    return render(request, 'taborniki/search_results.html', {'clan': clan})


def get_vod(request, vod_id):
    vod = Vod.objects.get(id=vod_id)
    vsiclani = vod.vod_clan.all()

    return render(request, 'taborniki/vod.html', {'vod': vod, 'clani': vsiclani, 'form': DodajClanaVodu})


def get_rod(request, rod_id):
    rod = Rod.objects.get(id=rod_id)
    vodi = rod.rodov_vod.all()
    clani_po_vodih = [['VOD','ST CLANOV']]
    for vod in vodi:
        clani_po_vodih.append([vod.imeVod, len(vod.vod_clan.all())])


    print(clani_po_vodih)
    return render(request, 'taborniki/rod.html', {'rod': rod, 'vodi': vodi, 'clani_po_vodih': json.dumps(clani_po_vodih)})


def dodajClan(request):
    if request.method == 'POST':
        print('nekej')
        form = DodajClan(request.POST)
        print(request)
        print(form)
        print(form.is_valid())
        # check whether it's valid:
        if form.is_valid():
            print('valid form')
            data = form.cleaned_data
            clan = Oseba.objects.create(ime=data['ime'], priimek=data['priimek'], naslov=data['naslov'],
                                        telefon=data['telefon'], email=data['email'], rojstvo=data['rojstvo'], vod = data['vod'])
            clan.save()

            return redirect('/taborniki/profil/%s' % clan.id)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = DodajClan()

    return render(request, 'taborniki/dodajClan.html', {'form': form})


def odstrani_clan(request, clan_id):
    print('odrstanjujem')
    clan = Oseba.objects.get(id=clan_id)
    clan.delete()
    return redirect('/taborniki/index')


def get_akcija(request, akcija_id):
    akcija = Akcija.objects.get(id=akcija_id)
    akcijaudelezenci = akcija.udelezenci.all()
    return render(request, 'taborniki/akcija.html', {'akcija': akcija, 'akcijaudelezenci': akcijaudelezenci})


def dodaj_clana_vodu(request, vod_id):
    form = DodajClanaVodu(request.GET)
    if form.is_valid():
        clan = form.cleaned_data['izbrani_clan']
        vod = Vod.objects.get(id=vod_id)
        clan.vod = vod
        clan.save()
        return redirect('/taborniki/vod/%s' % vod_id)
    else:
        return redirect('/taborniki/vod/%s' % vod_id)
