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


def buscar_pedido(request):
    if request.method == 'POST':
        form = BuscarPedidoForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero']
            nome_cliente = form.cleaned_data['nome_cliente']
            endereco = form.cleaned_data['endereco']

        #essa parte busca o pedido:
        try:
            pedido = Pedido.objects.get(id=numero, nome_cliente = nome_cliente, endereco = endereco)
            return redirect('pedido_feito',pedido_id = pedido.id)

        except Pedido.DoesNotExist:
            form.add_error(None,'Pedido não encontrado com as informações fornecidas')
    else:
        form = BuscarPedidoForm()

    return render(request, 'pizzaria/buscar_pedido.html', {'form':form})    
def home(request):
    return render(request,'pizzaria/home.html')

