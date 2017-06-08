# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from taborniki.models import Oseba
from django.db.models import Q
from .forms import NameForm

def index(request):
    return render(request,'taborniki/index.html' )

def clani(request):
    clani = Oseba.objects.all()
    output = ', '.join([p.__str__() for p in clani])
    return HttpResponse(output)

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            qs = Oseba.objects.all()
            qs = qs.filter(Q(ime=data['ime']) | Q(priimek=data['priimek']))
            clan = Oseba.objects.get(ime = data['ime'], priimek=data['priimek'])
            return render(request, 'taborniki/search_results.html', {'clan': clan})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'taborniki/name.html', {'form': form})