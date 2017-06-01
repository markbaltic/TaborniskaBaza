# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse
from taborniki.models import Oseba

def index(request):
    return HttpResponse("Hello, world. You're at the taborniki index.")

def clani(request):
    clani = Oseba.objects.all()
    output = ', '.join([p.__str__() for p in clani])
    return HttpResponse(output)