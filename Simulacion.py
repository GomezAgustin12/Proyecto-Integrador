import numpy as np
import pandas as pd
import doctest

import Aula
Aula=Aula.Aula
import Franja 
Franja=Franja.Franja
import Materias
Materia= Materias.Materia

class Simulacion:
    def __init__(self, data):
        self.excelMateria=pd.read_excel(data, "Materia")
        self.excelAula=pd.read_excel(data, "Aula")
        self.aulas=[]
        self.materias=[]
        self.crearAulas()

    
    def simulacionFranjaDia(self, franja, dia):
        self.fran=Franja(franja, dia)
        """
        >>>simulacionFranjaDia("Mañana", "Lunes")
        """


        if franja=="Mañana":
            i=0
            while self.excelMateria.Año[i]==1:
                self.materias.append(Materia(self.excelMateria.CodigoMateria[i], self.excelMateria.Facultad[i], self.excelMateria.Carrera[i], self.excelMateria.Nombre[i], self.excelMateria.Año[i], self.excelMateria.Semestre[i], self.excelMateria.CantHs[i], self.excelMateria.CantAlumnos[i]))
                i=i+1
        elif franja=="Tarde":
            i=0
            while self.excelMateria.Año[i]==2 and self.excelMateria.Año[i]==4:
                self.materias.append(Materia(self.excelMateria.CodigoMateria[i], self.excelMateria.Facultad[i], self.excelMateria.Carrera[i], self.excelMateria.Nombre[i], self.excelMateria.Año[i], self.excelMateria.Semestre[i], self.excelMateria.CantHs[i], self.excelMateria.CantAlumnos[i]))
                i=i+1
        else:
            i=0
            while self.excelMateria.Año[i]==3 and self.excelMateria.Año[i]==5:
                self.materias.append(Materia(self.excelMateria.CodigoMateria[i], self.excelMateria.Facultad[i], self.excelMateria.Carrera[i], self.excelMateria.Nombre[i], self.excelMateria.Año[i], self.excelMateria.Semestre[i], self.excelMateria.CantHs[i], self.excelMateria.CantAlumnos[i]))
                i=i+1


    def crearAulas(self):
        for x in self.excelAula.CodigoAula:
            self.aulas.append(Aula(self.excelAula.CodigoAula[x], self.excelAula.Piso[x], self.excelAula.Capacidad[x], self.excelAula.Descripcion[x]))
            

sim= Simulacion("E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Tablas.xlsx")

sim.simulacionFranjaDia("Mañana", "Lunes")


