import numpy as np
import pandas as pd

import Carrera
Carrera=Carrera.Carrera
import Materias


class Inicio:
    def __init__ (self, excel):
        self.ex=pd.read_excel(excel)

    def crearCarreras(self, nombre):
        self.carreras= Carrera(nombre)

    def crearMaterias(self, nombre)
        self.materias= Materia(nombre)

inicio= Inicio("E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Materias.xlsx")
inicio.crearCarreras(inicio.ex.Carrera)
inicio.crearMaterias(inicio.ex.Materia)