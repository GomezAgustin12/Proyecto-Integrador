import Carrera
Carrera=Carrera.Carrera

class Facultad:
    def __init__(self, nombre):
        self.nombre= nombre
        self.carreras=[]

    def crearCarrera(self, nombre):
        aux= Carrera(nombre)
        self.carreras.append(aux)
