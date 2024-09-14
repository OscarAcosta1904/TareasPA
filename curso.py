class Curso:
    nombre_curso = ""
    codigo_curso = 0
    instructor = ""
    
    curso = []
    
    def __init__(self, nombre_curso, codigo_curso,instructor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor
        
    def mostrar_info_curso(self):
        
        print("\n_____información del curso_____\n")
        
        for curso in self.curso:
            print("\n")
            print("codigo del curso: ", self.codigo_curso)
            print("nombre del curso: ", self.nombre_curso)
            print("instructor: ", self.instructor)
            
        
    