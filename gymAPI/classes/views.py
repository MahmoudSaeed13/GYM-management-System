from django.shortcuts import render
from classes.models import Class

# Create your views here.


def index(request):
    c = Class.objects.all()
    return render(request, 'classes/classes.html', context={'classes':c})