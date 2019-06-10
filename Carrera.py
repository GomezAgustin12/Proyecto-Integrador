import Materias
Materia= Materias.Materia
class Carrera:
    def __init__(self, nombre):
        self.nombre=nombre
        self.materias=[]

    def crearMateria(self, nombre, semestre):
        aux= Materia(nombre, semestre)
        self.materias.append(aux)
