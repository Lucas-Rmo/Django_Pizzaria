from django import forms
from .models import *

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome_cliente','endereco','borda','pizza1','pizza2']

        widgets = {
            'nome_cliente' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome'}),
            'endereco' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Endereço'}),
            'borda' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo de borda'}),
            'pizza1' : forms.Select(attrs={'class': 'form-control select-pizza', 'placeholder': 'Sabor 1'}),
            'pizza2' : forms.Select(attrs={'class': 'form-control select-pizza', 'placeholder': 'Sabor 2(opcional)'}),

        }

class BuscarPedidoForm(forms.Form):
    numero = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    nome_cliente = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    endereco = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control'}))

