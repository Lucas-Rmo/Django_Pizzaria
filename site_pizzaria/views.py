from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .forms import *
from .models import *

from .models import *
# Create your views here.

class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizzaria/cardapio.html'
    context_object_name = 'pizzas'


        
def pedido_form(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.preco = pedido.calcular_preco()
            pedido.save()
            return redirect('pedido_feito',pedido_id=pedido.id)
    else:
        form = PedidoForm
    
    return render(request,'pizzaria/pedido.html',{'form':form})
    
def pedido_concluido(request,pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    return render(request, 'pizzaria/pedido_feito.html', {'pedido':pedido})

