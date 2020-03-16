from django.shortcuts import render, redirect, get_object_or_404
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


def edytuj_wartosc(request, id):
    wartosc1 = get_object_or_404(Wplyw, pk=id)
    wartosc = FlowForm(request.POST or None, instance=wartosc1)

    if wartosc.is_valid():
        wartosc.save()
        return redirect(lista)

    return render(request, 'nowa_wartosc.html', {'wartosc': wartosc})


def kasuj_wartosc(request, id):
    wartosc1 = get_object_or_404(Wplyw, pk=id)

    if request.method == 'POST':
        wartosc1.delete()
        return redirect(lista)

    return render(request, 'potwierdz.html', {'wartosc1': wartosc1})
