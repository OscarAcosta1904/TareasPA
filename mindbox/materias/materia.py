class Materia:
    id: int #"MT{ultimos 2 digitos del nombre}{semestre}{cantidad creditos}{random(1, 1000)}": 
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