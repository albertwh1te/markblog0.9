from django import forms

class searchform(forms.Form):
    keywords = forms.CharField(max_length=100)

