
"""Определяет схемы URL для uc_links."""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # Вывод всех пользователей и их карт
    url(r'^users_and_cards/$', views.users_and_cards, name='users_and_cards'),
    ] 