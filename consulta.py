import random

class Consulta:
    id = 0
    fecha_hora = ""
    consultorio = ""
    medico = ""
    paciente = ""

    def __init__(self, fecha_hora, consultorio, medico, paciente):
        self.id = random.randint(1, 100)
        self.fecha_hora = fecha_hora
        self.consultorio = consultorio
        self.medico = medico
        self.paciente = paciente