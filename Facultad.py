import Carrera
Carrera=Carrera.Carrera

class Facultad:
    def __init__(self, nombre):
        self.nombre= nombre
        self.carreras=[]

    def CrearCarrera(self, nombre):
        aux= Carrera(nombre)
        self.carreras.append(aux)


ing = Facultad("Ingenieria y Tecnologia")
ing.CrearCarrera("Ingenieria en sistemas")
print(ing.carreras[0].nombre)
