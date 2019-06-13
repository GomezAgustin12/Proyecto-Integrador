import Hora
Hora=Hora.Hora

class Dia:
    def __init__(self, nombre, franja):
        self.nombre=nombre
        self.horas=[]
        self.crearHoras()

    def crearHoras(self):
        self.horas.append(Hora())