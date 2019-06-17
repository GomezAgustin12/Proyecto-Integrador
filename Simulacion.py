import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import pandas as pd
import random


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


            tablaMañana = {
                '8:30':[],
                '9':[],
                '9:30':[],
                '10':[],
                '10:30':[],
                '11':[],
                '11:30':[],
                '12':[]
            }
            i=0
            """for x in tablaMañana:
                for y in self.fran.dia.horas[i].aulas:
                    materiaAleatoria=random.randrange(0, len(self.materias))
                    tablaMañana[x].append(self.materias[materiaAleatoria].nombre)
                    self.materias.pop(materiaAleatoria)
                    if len(self.materias)==0:
                        break
                i=i+1"""

            materiasTabla=self.materias
            for x in self.materias:
                aleatorioMateria=random.randrange(0, len(materiasTabla))
                modulo=self.resolucionHoras(materiasTabla[aleatorioMateria])
                aleatorioAula=random.randrange(0, len(self.fran.dia.aulas))
                disponibilidad=self.fran.dia.aulas[aleatorioAula].disponibilidad()




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
        

sim= Simulacion()
sim.simulacionFranjaDia("Mañana", "Lunes")