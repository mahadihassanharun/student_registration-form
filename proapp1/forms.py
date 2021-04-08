from django import forms

class user_form(forms.Form):
    name = forms.CharField(max_length=30)
    email= forms.CharField(max_length=50)
    phone=forms.CharField(max_length=15)
