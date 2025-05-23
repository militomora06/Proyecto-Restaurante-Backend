import csv
from app.models import Producto  # Reemplaza `app` por el nombre de tu aplicación

with open('productos.csv', newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        Producto.objects.create(
            nombre=fila['Nombre'],
            descripcion=fila['Descripcion'],
            precio=fila['Precio'],
            categoria=fila['Categoria'],
            imagen=fila['Imagen']
        )
