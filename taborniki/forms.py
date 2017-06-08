from django import forms

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