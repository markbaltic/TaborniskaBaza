# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from taborniki.models import Oseba
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
            field = Oseba.objects.all().filter(ime = data['your_name'])
            return HttpResponse(field)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'taborniki/name.html', {'form': form})