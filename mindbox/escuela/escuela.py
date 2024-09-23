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
        self.lista_maestros.append(maestro)
        
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
        
    def listar_estudiantes(self):
        print("_____ESTUDIANTES_____")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())
    
    def listar_maestros(self):
        print("_____MAESTROS_____")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())
            
    def listar_materias(self):
        print("_____MATERIAS_____")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
            
    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove()
                print("Estudiante eliminado")
                return
            
        print(f"No se encontró el estudiante con número de control: {numero_control}")        
        
    