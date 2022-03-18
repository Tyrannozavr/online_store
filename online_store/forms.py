from django import forms

class Registration(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)