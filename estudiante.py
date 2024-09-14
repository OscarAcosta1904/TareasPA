import random

curso = []

class Estudiante:
    id_estudiante = 0
    nombre = ""
    edad = 0
    cursos = 0
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.id_estudiante = random.randint(1, 1000)
        self.cursos = []
        
    def agregar_curso(self, curso):
        self.cursos.append(curso)
    
    def mostrar_informacion(self):
        print("_____informacion del alumno_____")
        print("\n")
        print("id: ", self.id_estudiante)
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)
        print("cursos: ", self.cursos)
        
    
    
    