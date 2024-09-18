import random

class Paciente:
    id: int 
    nombre: str
    ano_nacimiento: int 
    peso: float
    estatura: float
    direccion: str

    def __init__(self, nombre: str, ano_nacimiento: int, peso: int, estatura: float, direccion: str):
        self.id = random.randint(1, 100)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion

    def mostrar_informacion(self):
        print(f"\nId: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Año de nacimiento: {self.ano_nacimiento}")
        print(f"Peso: {self.peso}")
        print(f"Estatura: {self.estatura}")
        print(f"Dirección: {self.direccion}")