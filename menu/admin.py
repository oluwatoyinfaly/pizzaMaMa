from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    '''Pizza admin'''
    list_display = ('name', 'price', 'ingredients', 'vegetarian')
    search_fields = ('name', 'ingredients')
# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
