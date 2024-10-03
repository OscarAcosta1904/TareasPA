from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    rfc: str
    sueldo: float
    ano_nacimiento: int
    
    def __init__(self, numero_control: str,nombre: str, apellido: str, rfc: str, sueldo: float, ano_nacimiento: int, contrasenia: str):
        super().__init__(nombre=nombre, numero_control=numero_control, apellido=apellido, contrasenia=contrasenia, rol=Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo
        self.ano_nacimiento = ano_nacimiento
        
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Número de control: {self.numero_control}\nNombre completo: {nombre_completo}\nRFC: {self.rfc}\nAño de nacimiento: {self.ano_nacimiento}\nSueldo: {self.sueldo}"
        return info