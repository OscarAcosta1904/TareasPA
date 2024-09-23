class Materia:
    id: int 
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    
    def __init__(self, id, nombre, descripcion, semestre, creditos):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos 
        
    def mostrar_info_materia(self):
        info = f"id: {self.id}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nSemestre: {self.semestre}\nCreditos: {self.creditos}"
        return info