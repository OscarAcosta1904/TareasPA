import random

class Medico:
    id: int
    nombre: str
    ano_nacimiento: int 
    rfc: str
    direccion: str

    def __init__(self, nombre: str, ano_nacimiento: int, rfc: str, direccion: str):
        self.id = random.randint(1, 100)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.direccion = direccion
        
    def mostrar_informacion(self):
        print(f"\nId: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Año de nacimiento: {self.ano_nacimiento}")
        print(f"rfc: {self.rfc}")
        print(f"Dirección: {self.direccion}")
