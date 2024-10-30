from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Borda)


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'endereco', 'pizza1', 'pizza2','borda', 'preco', 'status', 'marcar_como_concluido')
    list_filter = ('status',)
    search_fields = ('nome_cliente', 'endereco')

    # Define a ação personalizada
    actions = ['marcar_pedidos_como_concluido']

    def marcar_como_concluido(self, obj):
        if obj.status != 'Pedido entregue':
            return 'Pedido não concluido'
        return 'Concluído'
    marcar_como_concluido.allow_tags = True
    marcar_como_concluido.short_description = 'Ações'

    # Função para marcar pedidos como "Pedido entregue"
    def marcar_pedidos_como_concluido(self, request, queryset):
        queryset.update(status='Pedido entregue')
    marcar_pedidos_como_concluido.short_description = 'Marcar pedidos selecionados como concluído'


admin.site.register(Pedido,PedidoAdmin)