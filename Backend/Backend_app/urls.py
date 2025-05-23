from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, PedidoViewSet, registro, login_usuario

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', registro, name='registro'),
    path('login/', login_usuario, name='login_usuario'),
    
]
router.register(r'productos', ProductoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
import csv
from django.core.management.base import BaseCommand
from menu.models import Producto

class Command(BaseCommand):
    help = 'Importa productos desde un archivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('archivo', type=str)

    def handle(self, *args, **kwargs):
        archivo = kwargs['archivo']
        with open(archivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Producto.objects.create(
                    nombre=row['Nombre'],
                    descripcion=row['Descripcion'],
                    precio=row['Precio'],
                    categoria=self.normalizar_categoria(row['Categoria']),
                    imagen=row['Imagen']
                )
        self.stdout.write(self.style.SUCCESS('¡Productos importados exitosamente!'))

    def normalizar_categoria(self, categoria):
        mapa = {
            'entrada': 'entrada',
            'Platos Fuertes': 'fuerte',
            'Postre': 'postre',
            'Postres': 'postre',
            'Bebidas': 'bebida'
        }
        return mapa.get(categoria.strip(), 'entrada')

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('menu.urls')),

]
