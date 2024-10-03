from .utils.roles import Rol

class Usuario:
    nombre: str
    numero_control: str
    apellido: str
    contrasenia: str
    rol: Rol
    
    def __init__(self, nombre: str, numero_control: str, apellido: str, contrasenia: str, rol: Rol):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = contrasenia
        self.rol = rol