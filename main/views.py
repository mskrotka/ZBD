from django.shortcuts import render
from django.http import HttpResponse
from .models import Wplyw


# Create your views here.
def lista(request):
    obrot = Wplyw.objects.all()
    return render(request, 'lista.html', {'rotation': obrot})
