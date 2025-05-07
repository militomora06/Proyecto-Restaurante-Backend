from django.urls import path
from .views import ProductoListView, PedidoCreateView

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('pedidos/', PedidoCreateView.as_view(), name='pedido-create'),
]
