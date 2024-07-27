from django.shortcuts import render
from .models import *

def home(request):
    context = {
            'context': Homework.objects.all().values(),
            }
    return render(request, 'index.html', context=context)
