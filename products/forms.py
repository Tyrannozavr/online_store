from django import forms
from .models import Discount

class AllowDiscount(forms.Form):
    choice_two = None

    choices = [(i.name, str(i.discount)) for i in Discount.objects.all()]

    # print(choices)
    discount = forms.ChoiceField(choices=choices)