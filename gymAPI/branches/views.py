from django.shortcuts import render
from branches.models import Branch

# Create your views here.


def index(request):
    c = Branch.objects.all()
    return render(request, 'branches/branches.html', context={'branches':c})