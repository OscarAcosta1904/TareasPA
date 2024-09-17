from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Avenida Madero") # 5
paciente_tres = Paciente ("Carlos", 2010, 56, 1.52, "Clapham Common")

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8
medico_2 = Medico("Oscar", 1985, "3664687DF", "Aerolínea Carrillo")

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_paciente(paciente=paciente_tres)

hospital.registrar_medico(medico=medico)
hospital.registrar_medico(medico=medico_2)

contador = 0
while True:
    print("*** BIENVENIDO ***")
    print("opciones del sistema")
    print("1. mostrar pacientes")
    print("2. mostrar pacientes menores de edad")
    print("3. mostrar pacientes mayores de edad")
    print("4. mostrar medicos")
    print("5. eliminar paciente")
    print("6. eliminar medico")
    
    opcion = int(input("ingresa la opción que deseas: "))
    
    if opcion == 1:
        hospital.mostrar_pacientes()
        
    elif opcion == 2:
        hospital.mostrar_paciente_menores()
        
    elif opcion == 3:
        hospital.mostrar_pacientes_mayores()
        
    elif opcion == 4:
        hospital.mostrar_medicos()
        
    elif opcion == 5:
        hospital.eliminar_paciente()
        
    elif opcion == 6:
        hospital.eliminar_medico()
        
    else:
        print("\nadios")
        break


