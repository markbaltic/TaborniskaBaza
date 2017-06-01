# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models



# Create your models here.

class Clan(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name
class Oseba(models.Model):
    ime = models.CharField(max_length=50)
    priimek = models.CharField(max_length=50)
    naslov =models.CharField(max_length=100)
    rojstvo = models.DateField()
    telefon = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.ime +' '+ self.priimek


class Druzina(models.Model):
    imeDruzina = models.CharField(max_length=50)
    druzina = models.ForeignKey(Oseba,
                                on_delete=models.CASCADE,
                                related_name='druzina_clan')

class Rod(models.Model):
    imeRod = models.CharField(max_length=50)
    sedez = models.CharField(max_length=50)
    nacelnikRod = models.OneToOneField(Oseba,
                                       on_delete=models.CASCADE,
                                       related_name='+',)
    staresinaRod = models.OneToOneField(Oseba,
                                       on_delete=models.CASCADE,
                                       related_name='+',)
    clani = models.ForeignKey(Oseba,
                              on_delete=models.CASCADE,
                              related_name='rod_clan')

class Vod(models.Model):
    imeVod = models.CharField(max_length=50)
    vodnik = models.OneToOneField(Oseba,
                                       on_delete=models.CASCADE,
                                       related_name='+',)
    rod = models.OneToOneField(Oseba,
                                       on_delete=models.CASCADE,
                                       related_name='+',)
    clani = models.ForeignKey(Oseba,
                              on_delete=models.CASCADE,
                              related_name='vod_clan')

class Akcije(models.Model):
    imeAkcija = models.CharField(max_length=50)
    porocilo = models.FileField
    zacetek = models.DateTimeField
    konec = models.DateTimeField
    organizator = models.OneToOneField(Oseba)
    udelezenci = models.ForeignKey(Oseba,
                                   on_delete=models.CASCADE,
                                   related_name='akcija_clan')

class Clanarine(models.Model):
    leto = models.DateField
    clan = models.ForeignKey(Oseba,
                             on_delete=models.CASCADE,
                             related_name='clanarina_clan')