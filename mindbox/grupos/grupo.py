from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia

class Grupo:
    id: int
    estudiantes: List[Estudiante] = []
    maestros: List[Maestro] = []
    materias : list[Materia] = []
    tipo: chr   
    
    def __init__(self):
        pass