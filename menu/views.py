from django.shortcuts import render
#from django.http import HttpResponse
from .models import Pizza

# Create your views here.
def index(request):
    '''Index view'''
    pizzas = Pizza.objects.all()
    '''pizzas_names_and_prices = [pizza.name + ' : ' + str(pizza.price) + '€' for pizza in pizzas]
    pizzas_names_and_price_strs = ', '.join(pizzas_names_and_prices)
    return HttpResponse('Les pizzas: '+ pizzas_names_and_price_strs)'''
    return render(request, 'menu/index.html', {'pizzas': pizzas})
