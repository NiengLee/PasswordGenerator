from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generatedPass = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numeros'):
        characters.extend(list('1234567890'))

    if request.GET.get('especial'):
        characters.extend(list('|°!"#$%&/()=?¡¿´+{}[],.*/-;:_<>¬|@·~½¬`^'))

    for x in range(length):
        generatedPass += random.choice(characters)

    return render(request, 'password.html', {'Password': generatedPass})