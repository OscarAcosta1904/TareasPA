from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime

escuela = Escuela()

while True:
    print("_____MINDBOX_____")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")
    
    opcion = input("Ingresa una opción para continuar: ")
    
    if opcion == "1":
        print("\nSeleccionaste la opción para registrar un estudiante")
        
        numero_control = escuela.generar_numero_control_estudiante()
        print(numero_control)
        nombre = input("ingresa el nombre del estudiante: ")
        apellido = input("ingresa el apellido del estudiante: ")
        curp = input("ingresa el curp del estudiante: ")
        ano = int(input("ingresa el año de nacimiento del estudiante: "))
        mes = int(input("ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("ingresa el día de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        
        
    
    elif opcion == "2":
        print("\nSeleccionaste la opción registar maestro")
        
        nombre = input("ingresa el nombre del maestro: ")
        apellido = input("ingresa el apellido del maestro: ")
        rfc = input("ingrese el rfc del maestro: ")
        sueldo = float(input("ingrese el sueldo del maestro: "))
        ano = int(input("ingresa el año de nacimiento del maestro: "))
        
        numero_control = escuela.generar_numero_control_maestro(nombre=nombre, rfc=rfc, ano=ano)
        print(numero_control)

    
    elif opcion == "3":
        print("\nSeleccionaste la opción reagistrar materia")
        
        nombre = input("ingresa el nombre de la materia: ")
        descripcion = input("ingrase la descripción de la materia: ")
        semestre = int(input("semestre: "))
        creditos = int(input("cantidad de creditos: "))
        
        numero_control = escuela.generar_numero_control_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print(numero_control)
    
    elif opcion == "4":
        pass
    
    elif opcion == "5":
        pass
    
    elif opcion == "6":
        print("\nadios popo")
        break