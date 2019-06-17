import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import pandas as pd
import random
from datetime import datetime, date, time, timedelta

import Franja 
Franja=Franja.Franja
import Materias
Materia= Materias.Materia

flag=True

class Simulacion:
    def __init__(self):
        
        self.materias=[]
    
    def simulacionFranjaDia(self, franja, dia):
        self.fran=Franja(franja, dia)
        excelMateria=pd.read_excel("E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Tablas.xlsx", "Materia")
        if franja=="Mañana":
            i=0
            for m in excelMateria.Año:    
                if m==1:
                    self.materias.append(Materia(excelMateria.CodigoMateria[i], excelMateria.Facultad[i], excelMateria.Carrera[i], excelMateria.Nombre[i], excelMateria.Año[i], excelMateria.Semestre[i], excelMateria.CantHs[i], excelMateria.CantAlumnos[i]))
                    i=i+1


            materiasTabla=self.materias
            for x in self.materias:
                aleatorioMateria=random.randrange(0, len(materiasTabla))
                modulo=self.resolucionHoras(materiasTabla[aleatorioMateria])
                aleatorioAula=random.randrange(0, len(self.fran.dia.aulas))
                disponibilidad=self.fran.dia.aulas[aleatorioAula].disponibilidad()
                self.asignacion(disponibilidad, aleatorioAula)




        elif franja=="Tarde":
            i=0
            while excelMateria.Año[i]==2 and excelMateria.Año[i]==4:
                self.materias.append(Materia(excelMateria.CodigoMateria[i], excelMateria.Facultad[i], excelMateria.Carrera[i], excelMateria.Nombre[i], excelMateria.Año[i], excelMateria.Semestre[i], excelMateria.CantHs[i], excelMateria.CantAlumnos[i]))
                i=i+1
        else:
            i=0
            while excelMateria.Año[i]==3 and excelMateria.Año[i]==5:
                self.materias.append(Materia(excelMateria.CodigoMateria[i], excelMateria.Facultad[i], excelMateria.Carrera[i], excelMateria.Nombre[i], excelMateria.Año[i], excelMateria.Semestre[i], excelMateria.CantHs[i], excelMateria.CantAlumnos[i]))
                i=i+1

    def resolucionHoras(self, mt):
        cantHs=mt.cantHs
        if cantHs==4:
            modulo1=2
            modulo2=2
        elif cantHs==5:
            if flag==True:
                modulo1=3
                modulo2=2
                flag=False
            else:
                modulo1=2
                modulo2=3
                flag=True
        else:
            modulo1=3
            modulo2=3
        return modulo1

    def asignacion(self, disponibilidad, aleatorioAula):
        if disponibilidad==time(7, 30):
            self.fran.dia.aulas[aleatorioAula].hora[0].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[1].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[2].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[3].asignado=True
        elif disponibilidad==time(9, 30):
            self.fran.dia.aulas[aleatorioAula].hora[4].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[5].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[6].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[7].asignado=True
        elif disponibilidad==time(10, 30):
            self.fran.dia.aulas[aleatorioAula].hora[8].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[9].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[10].asignado=True
            self.fran.dia.aulas[aleatorioAula].hora[11].asignado=True
            self.fran.dia.aulas.pop(aleatorioAula)

sim= Simulacion()
sim.simulacionFranjaDia("Mañana", "Lunes")