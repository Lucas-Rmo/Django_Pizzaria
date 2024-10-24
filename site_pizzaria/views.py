from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView

from .models import *
# Create your views here.

class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizzaria/cardapio.html'
    context_object_name = 'pizzas'