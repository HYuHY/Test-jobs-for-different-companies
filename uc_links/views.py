from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Person, Cards
from .forms import PersonForm, CardsForm, PersonCardForm

def index(request):
    """Домашняя страница приложения uc_links"""
    form_user = PersonForm()
    form_card = CardsForm()
    form_user_card = PersonCardForm()
    # Отправлены данные POST; обработать данные.
    if request.POST.get('form0'):
        form_user = PersonForm(request.POST)
        if form_user.is_valid():
            form_user.save()
    elif request.POST.get('form1'):
        form_card = CardsForm(request.POST)
        if form_card.is_valid():
            form_card.save()
    elif request.POST.get('form2'):
        form_user_card = PersonCardForm(request.POST)
        user = request.POST.get('user', default=None)
        card = request.POST.get('card', default=None)
        if user != None and card != None:
            user = get_object_or_404(Person, pk=user)
            card = get_object_or_404(Cards, pk=card)
            card.person = user
            card.save()
    form = [form_user, form_card, form_user_card]
    context = {'form': form}
    return render(request, 'uc_links/index.html', context)


def users_and_cards(request):
    """Выводит всех пользователей и их карты"""
    users = Person.objects.order_by('last_name')
    uc_dict = {}
    for user in users:
        if user.cards_set.exists():
            uc_dict[user] = len(user.cards_set.all())
        else:
            uc_dict[user] = 0
            
    context = {'uc_dict': uc_dict}
    return render(
        request, 
        'uc_links/users_and_cards.html', 
        context
        )

