from django.urls import path
from .views import lista, nowa_wartosc, edytuj_wartosc, kasuj_wartosc

urlpatterns = [
    path('lista/', lista, name='lista_wszystkiego'),
    path('dodaj-nowa-wartosc/', nowa_wartosc, name='nowa_wartosc'),
    path('edycja/<int:id>', edytuj_wartosc, name='edytuj_wartosc'),
    path('kasuj/<int:id>', kasuj_wartosc, name='kasuj_wartosc')
  ]
