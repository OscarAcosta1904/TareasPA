from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

# paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero") # 5
# paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Avenida Madero") # 5
# paciente_tres = Paciente ("Carlos", 2010, 56, 1.52, "Clapham Common")

# medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8
# medico_2 = Medico("Oscar", 1985, "3664687DF", "Aerolínea Carrillo")

# hospital.registrar_paciente(paciente=paciente)
# hospital.registrar_paciente(paciente=paciente_dos)
# hospital.registrar_paciente(paciente=paciente_tres)

# hospital.registrar_medico(medico=medico)
# hospital.registrar_medico(medico=medico_2)

contador = 0
while True:
    print("\n*** BIENVENIDO ***")
    print("opciones del sistema")
    print("1. registrar paciente")
    print("2. registrar medico")
    print("3. mostrar pacientes")
    print("4. mostrar pacientes menores de edad")
    print("5. mostrar pacientes mayores de edad")
    print("6. mostrar medicos")
    print("7. eliminar paciente")
    print("8. eliminar medico")
    opcion = int(input("ingresa la opción que deseas: "))
    
    if opcion == 1:
        nombre = input("nombre: ") 
        ano_nacimiento = int(input("año de nacimiento: "))
        peso = float(input("peso: "))
        estatura = float(input("estatura: "))
        direccion = input("direccion: ")
        
        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente)
        print("paciente agregado correctamente :)")
        
    elif opcion == 2:
        nombre = input("nombre: ")
        ano_nacimiento = input("año de nacimiento: ")
        rfc = input("rfc: ")
        direccion = input("direccion: ")
        
        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico()
        print("medico agregado correctamente :)")
        
    
    elif opcion == 3:
        hospital.mostrar_pacientes()
        
    elif opcion == 4:
        hospital.mostrar_paciente_menores()
        
    elif opcion == 5:
        hospital.mostrar_pacientes_mayores()
        
    elif opcion == 6:
        hospital.mostrar_medicos()
        
    elif opcion == 7:
        hospital.eliminar_paciente()
        
    elif opcion == 8:
        hospital.eliminar_medico()
        
    else:
        print("\nadios")
        break
