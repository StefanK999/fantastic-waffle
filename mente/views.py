from django.shortcuts import render

# Create your views here.
def lista_pensieri(request):
    return render(request, 'mente/lista_pensieri.html', {})