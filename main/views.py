'''Main views'''
from django.shortcuts import render

# Create your views here.

def index(request):
    '''Index view'''
    return render(request, 'main/index.html')
