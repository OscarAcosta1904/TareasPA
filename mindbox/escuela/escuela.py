from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_grupos: List[Grupo] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        
    def generar_numero_control_estudiante(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes) + 1
        aleatorio = randint(0, 10000)
        
        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control
    
    def registrar_maestro(self, maestro: Maestro):
        self.lista_mestros.append(maestro)
        
    def generar_numero_control_maestro(self, rfc, nombre, ano):
        dia = datetime.now().day
        longitud = len(self.lista_maestros)
        aleatorio = randint(500, 5000)
        letras = nombre[:2].upper()
        rfc = rfc [-2:].upper()
        
        numero_control = f"M{ano}{dia}{aleatorio}{letras}{rfc}{longitud + 1}"
        return numero_control
    
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
        
    def generar_numero_control_materia(self, nombre, semestre, creditos):
        letras = nombre[-2:].upper()
        aleatorio = randint(1, 1000)
        
        numero_control = f"{letras}{semestre}{creditos}{aleatorio}"
        return numero_control