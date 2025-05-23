from rest_framework import serializers
from .models import Producto, Pedido, ItemPedido

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ItemPedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        source='producto',
        write_only=True
    )

    class Meta:
        model = ItemPedido
        fields = ['id', 'producto', 'producto_id', 'cantidad']


class PedidoSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True)
    usuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'nombre_cliente', 'telefono', 'direccion', 'valor_total', 'fecha', 'estado', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in items_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        return pedido
