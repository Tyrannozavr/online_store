from django import forms
from products.models import Products, Category

class Registration(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)

class CreateDiscount(forms.Form):
    choice = [(i.id, i.title) for i in Products.objects.all()]
    choice.extend(list([(i.id, i.title) for i in Category.objects.all()]))
    name = forms.CharField()
    size = forms.IntegerField(max_value=100, min_value=0)
    coverage = forms.ChoiceField(choices=((0, 'product'), (1, 'category')))
    products = forms.ChoiceField(choices=choice)
