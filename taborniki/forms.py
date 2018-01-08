from django import forms
from taborniki.models import  Oseba,Vod

class NameForm(forms.Form):
    ime = forms.CharField(label="ime", max_length=100, required=False, initial='')
    priimek = forms.CharField(label="priimek", max_length=100, required=False, initial='')

class DodajClan(forms.Form):
    ime = forms.CharField(label="ime", max_length=100, required=True)
    priimek = forms.CharField(label="priimek", max_length=100, required=True)
    naslov = forms.CharField(max_length=100)
    rojstvo = forms.DateField()
    telefon = forms.CharField(max_length=50)
    email = forms.EmailField()
    slika = forms.CharField(max_length=200)
    vod = forms.ModelChoiceField(queryset=Vod.objects.all())

class Search(forms.Form):
    q = forms.CharField(label = "q", max_length=100, required=True)

class DodajClanaVodu(forms.Form):
    izbrani_clan = forms.ModelChoiceField(queryset=Oseba.objects.all())
