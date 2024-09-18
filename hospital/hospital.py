from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta

class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_pacientes(self):
        print("*** Pacientes en el Sistema ***")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True
    
    
    def mostrar_medicos(self):
        print("*** Medicos en el Sistema***")
        for medico in self.medicos:
            medico.mostrar_informacion()
            
    def mostrar_paciente_menores(self):
        print("*** Pacientes menores de edad***")
        
        hay_menores = False
        
        for paciente in self.pacientes:
            if 2024 - paciente.ano_nacimiento < 18:
                paciente.mostrar_informacion()
                hay_menores = True
                
        if not hay_menores:
            print("no hay paciente menores de edad")
            
        return
    
    def mostrar_pacientes_mayores(self):
        print("*** Pacientes mayores de edad***")
        
        hay_mayores = False
        
        for paciente in self.pacientes:
            if 2024 - paciente.ano_nacimiento >= 18:
                paciente.mostrar_informacion()
                hay_mayores = True
                
        if not hay_mayores:
            print("no hay paciente mayores de edad")
            
        return
    
    
            
            
    def eliminar_paciente(self):
        id_paciente_a_eliminar = int(input("id de paciente a eliminar: "))
        for paciente in self.pacientes:
            if paciente.id == id_paciente_a_eliminar:
                self.pacientes.remove(paciente)
                print("se eliminó el paciente con el id: ", id_paciente_a_eliminar)
                break
            
    def eliminar_medico(self):
        id_medico_a_eliminar = int(input("id de medico a eliminar: "))
        for medico in self.medicos:
            if medico.id == id_medico_a_eliminar:
                self.pacientes.remove(medico)
                print("se eliminó el medico con el id: ", id_medico_a_eliminar)
                break