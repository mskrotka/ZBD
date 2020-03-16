from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wplyw
from .forms import FlowForm


# Create your views here.
def lista(request):
    obrot = Wplyw.objects.all()
    return render(request, 'lista.html', {'rotation': obrot})


def nowa_wartosc(request):
    wartosc = FlowForm(request.POST or None)

    if wartosc.is_valid():
        wartosc.save()
        return redirect(lista)

    return render(request, 'nowa_wartosc.html', {'wartosc': wartosc})