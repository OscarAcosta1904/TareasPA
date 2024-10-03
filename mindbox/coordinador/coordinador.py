from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: float 
    rfc: str
    anos_antiguedad: int
    
    def __init__(self, numero_control: int, nombre: str, apellido: str, contrasenia: str, sueldo: float, rfc: str, anos_antiguedad: int):
        super().__init__(nombre=nombre,
                         numero_control=numero_control,
                         apellido=apellido,
                         contrasenia=contrasenia,
                         rol=Rol.COORDINADOR)
        self.sueldo = sueldo
        self.rfc = rfc
        self.anos_antiguedad = anos_antiguedad
        
    def mostrar_info_coordiandor(self):
        # nombre_completo: f"{self.nombre} {self.apellido}"
        # info = f"Número de control: {self.numero_control}\nNombre: {nombre_completo}\nSueldo: {self.sueldo}\nrfc: {self.rfc}\nAños trabajando en la empresa: {self.anos_antiguedad}\nRol: {self.rol.value}"
        # return info
        pass
    