from django.urls import path
from .views import lista

urlpatterns = [
    path('ruch/', lista)
  ]
