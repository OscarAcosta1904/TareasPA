from typing import List
from producto.producto import Producto

class Tienda:
    lista_productos: List [Producto] = []
    
    def __init__(self) -> None:
        jitomates = Producto(id="123", nombre="Jitomates", precio=50, cantidad=6)
        lechuga = Producto(id="1234", nombre="Lechuga", precio=40, cantidad=1)
        squirt = Producto(id="1263", nombre="Squirt", precio=35, cantidad=8)
        chocolate = Producto(id="12693", nombre="Chocolate", precio=16, cantidad=10)
        

def agregar_producto(self, producto: Producto):
    self.lista_productos.append(producto) 