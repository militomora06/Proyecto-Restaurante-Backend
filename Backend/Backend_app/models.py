from django.db import models

class Producto(models.Model):
    CATEGORIAS = [
        ('entrada', 'Entrada'),
        ('fuerte', 'Plato Fuerte'),
        ('postre', 'Postre'),
        ('bebida', 'Bebida'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagen = models.URLField(blank=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
