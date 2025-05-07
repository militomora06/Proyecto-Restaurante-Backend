from rest_framework import serializers
from .models import Producto, Pedido, ItemPedido

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['producto', 'cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'nombre_cliente', 'telefono', 'direccion', 'valor_total', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        pedido = Pedido.objects.create(**validated_data)
        for item in items_data:
            ItemPedido.objects.create(pedido=pedido, **item)
        return pedido
