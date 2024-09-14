from estudiante import Estudiante
from curso import Curso

estudiante_1 = Estudiante("Julio", 8)
estudiante_2 = Estudiante("Sofia", 36)

curso_1 = Curso("matemáticas", 5, "Renata")
curso_2 = Curso("español", 7, "Gerardo")
curso_3 = Curso("historia", 10, "Rogelio")

estudiante_1.agregar_curso(curso_1)
estudiante_2.agregar_curso(curso_1)

estudiante_1.agregar_curso(curso_2)
estudiante_2.agregar_curso(curso_2)

estudiante_1.agregar_curso(curso_3)
estudiante_2.agregar_curso(curso_3)



estudiante = Estudiante("Juan", 8)

opcion = 0
while True:
    print("__bienvenido__")
    print("opciones en el sistema")
    print("1. agregar curso")
    print("2. mostrar inforamción del estudiante")
    print("3. mostrar información del curso")
    
    opcion = input("ingresa la opcion que deseas: ")
    
    if opcion == "1":
        id = int(input("ingresa id del curso: "))
        nombre = input("ingresa nombre del curso: ")
        instructor = input("ingresa el instructor del curso: ")
        
        curso = Curso(codigo_curso=id, instructor=instructor, nombre_curso=nombre)
        estudiante.agregar_curso(curso)
        print("\ncurso agregado correctamente")
        
    elif opcion == "2": 
        estudiante.mostrar_informacion()
    
    elif opcion == "3":
        curso.mostrar_info_curso()
