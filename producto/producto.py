from random import randint
from datetime import datetime, date

class Producto:
    id: int
    nombre: str
    precio: float 
    cantidad: int
    
    def __init__(self, int, nombre, precio, cantidad) -> None:
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
def generar_id(self, nombre, precio):
    letras_nombre = nombre[:2]
    letras_nombre.upper()
    dia = datetime.now().day
    aleatorio = randint(1, 100)
    
    id = f"{letras_nombre}{dia}{aleatorio}"
    
    return id 
    
        
def calcular_valor_total():
    pass

def mostrar_detalles():
    pass

