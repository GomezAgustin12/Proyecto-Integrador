import numpy as np
import pandas as pd

import Aula
Aula=Aula.Aula
import Franja 
Franja=Franja.Franja

class Simulacion:
    def __init__(self, data):
        self.excelMateria=pd.read_excel(data, "Materia")
        self.excelAula=pd.read_excel(data, "Aula")
        self.aulas=[]
        self.crearAulas()

    
    def simulacionFranjaDia(self, franja, dia):
        self.fran=Franja(franja, dia)

    def crearAulas(self):
        for x in self.excelAula.CodigoAula:
            self.aulas.append(Aula(self.excelAula.CodigoAula[x], self.excelAula.Piso[x], self.excelAula.Capacidad[x], self.excelAula.Descripcion[x]))
            print(self.aulas[x].capacidad)
            

sim= Simulacion("E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Tablas.xlsx")



