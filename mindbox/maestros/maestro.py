class Maestro:
    numero_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    ano_nacimiento: int
    
    def __init__(self, numero_control: str,nombre: str, apellido: str, rfc: str, sueldo: float, ano_nacimiento: int):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
        self.ano_nacimiento = ano_nacimiento
        
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Número de control: {self.numero_control}\nNombre completo: {nombre_completo}\nRFC: {self.rfc}\nAño de nacimiento: {self.ano_nacimiento}\nSueldo: {self.sueldo}"
        return info