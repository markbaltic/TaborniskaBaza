from django import forms

class NameForm(forms.Form):
    ime = forms.CharField(label="ime", max_length=100, required=False, initial='')
    priimek = forms.CharField(label="priimek", max_length=100, required=False, initial='')
