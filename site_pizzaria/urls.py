from django.contrib import admin
from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cardapio/',PizzaListView.as_view(),name='cardapio'),
    path('pedido/',pedido_form,name='pedido'),
    path('pedido/finalizado/<int:pedido_id>/',pedido_concluido,name='pedido_feito'),
    path('pedido/pesquisar/',buscar_pedido,name='buscar_pedido'),
    path('',home,name='home')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)