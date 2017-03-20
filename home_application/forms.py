from django import forms

class AddForm:
    ask = forms.CharField(max_length=256)
    answer = forms.CharField(max_length=256)