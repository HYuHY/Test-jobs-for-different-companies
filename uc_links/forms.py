from django import forms
from django.db import models

from .models import Person, Cards

tu_person = Person.objects.order_by('last_name')
tu_card = Cards.objects.order_by('card_number')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['last_name', 'first_name']
        labels = {'last_name': 'Last Name', 'first_name': 'First Name'}

class CardsForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ['card_number']
        labels = {'card_number': 'Card Number'}


class PersonCardForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Person.objects.all())
    card = forms.ModelChoiceField(queryset=Cards.objects.all())
    
        





