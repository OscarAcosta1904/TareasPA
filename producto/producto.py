from random import randint
from datetime import datetime

class Producto:
    ide: int
    nombre: str
    precio: float 
    cantidad: int
    
    def __init__(self, ide, nombre, precio, cantidad):
        self.ide = ide
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def generar_id(nombre):
        letras_nombre = nombre[:2]
        letras_nombre.upper()
        dia = datetime.now().day
        aleatorio = randint(1, 100)

        ide = f"{letras_nombre}{dia}{aleatorio}"

        return ide 
    
        
    def calcular_valor_total(): #Calcula el valor total del inventario para el producto 
        pass

    def mostrar_detalles(): #Devuelve los detalles del producto como un str ID, nombre, precio, cantidad, valor total en inventario
        pass

    def editar(): #Editar detalles del producto existente
        pass

