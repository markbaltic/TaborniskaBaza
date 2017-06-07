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
        if form.is_valid():
            clan = Oseba.objects.all().filter(ime = form)
            return HttpResponse(clan)
    else:
        form = NameForm()

    return render(request, 'clan.html', {'form': form})

from django.template import RequestContext
from django.shortcuts import render_to_response

def search(request):
    query = request.GET.get('id')
    results = None

    if query:
        results = Oseba.objects.get(uid=query)
    context = RequestContext(request)
    return render_to_response('taborniki/results.html', {"results": results,}, context_instance=context)