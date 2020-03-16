from django.urls import path
from .views import lista, nowa_wartosc

urlpatterns = [
    path('lista/', lista),
    path('dodaj-nowa-wartosc/', nowa_wartosc)
  ]
