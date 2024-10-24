from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView

from .models import *
# Create your views here.

class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizzaria/cardapio.html'
    context_object_name = 'pizzas'
=======

# Create your views here.
>>>>>>> 41233c522f3efcfcc1f270f196f754cbe2b96039
