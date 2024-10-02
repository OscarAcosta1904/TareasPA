from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from semestre.semestre import Semestre
from carrera.carrera import Carrera
from grupos.grupo import Grupo
from datetime import datetime

class Menu:
    escuela: Escuela = Escuela()
    # nombre_usuario: str = "juan123"
    # contraseña_usuario: str = "12345*"
    
    usuario_estudiante: str = "estudiante123"
    contraseña_estudiante: str = "estudiante123+"
    
    usuario_maestro: str = "maestro123"
    contraseña_maestro: str = "maestro123+"
    
    def login(self):
        
        intentos = 0
        while intentos<5:
            print("_____BIENVENIDO_____")
            print("Inicia sesión para continuar")

            nombre_usuario = input("\nIngresa tu nombre de usuario: ")
            contraseña_usuario = input("\nIngresa tu contraseña: ")
            
            if nombre_usuario == self.usuario_estudiante:
                if contraseña_usuario == self.contraseña_estudiante:
                    self.mostrar_menu_estudiante()
                    intentos = 0
                else:
                    intentos = self.mostarr_intento_sesion_fallido(intentos_usuario=intentos)
                    
            elif nombre_usuario == self.usuario_maestro:
                if contraseña_usuario == self.contraseña_maestro:
                    self.mostrar_menu_maestro()
                    intentos = 0
                else:
                    intentos = self.mostarr_intento_sesion_fallido(intentos_usuario=intentos)
                
            else:
                intentos = self.mostarr_intento_sesion_fallido(intentos_usuario=intentos)
                
                
        print("\nMáximos intentos de inicion de sesión equivoocados. adiós.")
        
    def mostarr_intento_sesion_fallido(self, intentos_usuario):
        print("\nUsuario o contraseña incorrectos. Intenta de nuevo.")
        return intentos_usuario + 1
        
    def mostrar_menu_estudiante(self):
        opcion = 0 
        while opcion != 3:
            print("\n_____MINDBOX_____")
            print("1. Ver horario")
            print("2. Ver grupos")
            print("3. Salir")
            
            opcion = int(input("\nIngresa una opción: "))
            
            if opcion == 3:
                break
    
    def mostrar_menu_maestro(self):
        opcion = 0
        while opcion != 5:
            print("\n_____MINDBOX_____")
            print("1. Ver horarios")
            print("2. Ver grupos")
            print("3. Ver materias")
            print("4. Ver alumnos")
            print("5. Salir")
            
            opcion = int(input("\nIngresa una opción: "))
            
            if opcion == 5:
                break
    
    def mostrar_menu(self):
        while True:
            print("_____MINDBOX_____")
            print("1. Registrar estudiante")
            print("2. Registrar maestro")
            print("3. Registrar materia")
            print("4. Registrar grupo")
            print("5. Registrar horario")
            print("6. Mostrar estudiantes")
            print("7. Mostrar maestros") 
            print("8. Mostrar materias") 
            print("9. Mostrar carrera") 
            print("10. Mostrar semestre") 
            print("11. Mostrar grupos")
            print("12. Eliminar estudiante")
            print("13. Eliminar maestro") 
            print("14. Eliminar materia") 
            print("15. Registrar carrera")
            print("16. Registrar semestre")
            print("17. Salir")

            opcion = input("Ingresa una opción para continuar: ")
    
            if opcion == "1":
                print("\nSeleccionaste la opción para registrar un estudiante")


                nombre = input("ingresa el nombre del estudiante: ")
                apellido = input("ingresa el apellido del estudiante: ")
                curp = input("ingresa el curp del estudiante: ")
                ano = int(input("ingresa el año de nacimiento del estudiante: "))
                mes = int(input("ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("ingresa el día de nacimiento del estudiante: "))
                fecha_nacimiento = datetime(ano, mes, dia)
                numero_control = self.escuela.generar_numero_control_estudiante()

                estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
                self.escuela.registrar_estudiante(estudiante=estudiante)



            elif opcion == "2":
                print("\nSeleccionaste la opción registar maestro")

                nombre = input("ingresa el nombre del maestro: ")
                apellido = input("ingresa el apellido del maestro: ")
                rfc = input("ingrese el rfc del maestro: ")
                sueldo = float(input("ingrese el sueldo del maestro: "))
                ano_nacimiento = int(input("ingresa el año de nacimiento del maestro: "))
                numero_control = self.escuela.generar_numero_control_maestro(rfc=rfc, nombre=nombre, ano=ano_nacimiento)

                maestro = Maestro(numero_control=numero_control, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo, ano_nacimiento=ano_nacimiento)
                self.escuela.registrar_maestro(maestro=maestro)

            elif opcion == "3":
                print("\nSeleccionaste la opción reagistrar materia")

                nombre = input("ingresa el nombre de la materia: ")
                descripcion = input("ingrase la descripción de la materia: ")
                semestre = int(input("semestre: "))
                creditos = int(input("cantidad de creditos: "))
                id = self.escuela.generar_numero_control_materia(nombre=nombre, semestre=semestre, creditos=creditos)

                materia = Materia(id=id, nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
                self.escuela.registrar_materia(materia=materia)

            elif opcion == "4":
                print("\nSeleccinoaste la opción para registrar un grupo")

                tipo = input("ingresa el tipo de grupo: ")
                id_semestre = input("ingresa el id del semstre al que pertenece el grupo: ")

                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)

                self.escuela.registrar_grupo(grupo=grupo)

            elif opcion == "5":
                pass
            
            elif opcion == "6":
                print("\nSeleccionaste la opción mostrar estudiantes")
                self.escuela.listar_estudiantes()

            elif opcion == "7":
                print("\nSeleccionaste la opción mostrar maestros")
                self.escuela.listar_maestros()

            elif opcion == "8":
                print("\nSeleccionaste la opción mostrar materias")
                self.escuela.listar_materias()

            elif opcion == "9":
                print("\nSeleccionaste la opción mostrar carreras")
                self.escuela.listar_carreras()

            elif opcion == "10":
                print("\nSeleccionaste la opcióno mostrar semestres")
                self.escuela.listar_semestres()

            elif opcion == "11":
                print("\nSeleccionaste la opción mostrar grupos")
                self.escuela.listar_grupos()

            elif opcion == "12":
                print("\nSeleccionaste la opción para eliminar un estudiante")
                numero_control = input("Ingresa el número de control del estudiante a eliminar: ")
                self.escuela.eliminar_estudiante(numero_control=numero_control)

            elif opcion == "13":
                print("\nSeleccionaste la opción eliminar un maestro")
                numero_control = input("Ingresa el número de control del maestro a eliminar: ")
                self.escuela.eliminar_maestro(numero_control=numero_control)

            elif opcion == "14":
                print("\nSeleccionaste la opción eliminar una materia")
                id = input("Ingresa el id de la materia a eliminar: ")
                self.escuela.eliminar_materia(id=id)

            elif opcion == "15":
                print("\nSeleccionaste la opción registrar una carrera")

                nombre = input("Ingresa el nombre de la carrera: ")
                carrera = Carrera(nombre=nombre)

            elif opcion == "16":
                print("\nSeleccinaste al opción para generar un semestre")

                numero = input("Ingresa el número del semestre: ")
                id_carrera = input("Ingresa el id de la carrera: ")
                semestre = Semestre(numero=numero, id_carrera=id_carrera)

                self.escuela.registrar_semestre(semestre=semestre)

            elif opcion == "17":
                print("\nadios")
                break