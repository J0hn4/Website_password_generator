from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'fsajowernzouoqeorewrjcnx'})

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    thepassword = 'testing'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        # upper =
        characters.extend([char.upper() for char in characters])

    if request.GET.get('numbers'):
        # numbers = [int(num) for num in list('1234567890')]
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()+=?/><~'))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password':thepassword})

