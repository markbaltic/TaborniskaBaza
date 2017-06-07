from django import forms

class NameForm(forms.Form):
    ime = forms.CharField(label="Your name", max_length=100)
