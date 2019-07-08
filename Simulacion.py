import numpy as np
import random
from datetime import datetime, date, time, timedelta
import pymongo

from UI import imagenes

import sys

import Franja 
Franja=Franja.Franja
import Materias
Materia= Materias.Materia

aulasDosModulos=0
aulasTresModulos=0

from PyQt5 import QtCore, QtGui, QtWidgets

class Simulacion:

    def simulacionFranjaDia(self, franja, dia):
        global aulasDosModulos
        global aulasTresModulos
        self.materiasNoAsignadasTresModulos=[]
        self.materias=[]
        self.materiasNoAsignadasDosModulos=[]
        self.fran=Franja(franja, dia)

        client = pymongo.MongoClient("mongodb+srv://nitsuga:nitsugagustin321@asignacionaulasucp-gf74h.mongodb.net/test?retryWrites=true&w=majority")
        db = client.Simulacion
        materia = db.Materia


        años=self.elegirFranja(franja, materia)
        for m in años:    
            self.materias.append(Materia(m["Facultad"], m["Carrera"], m["Nombre"], m["Año"], m["Semestre"], m["Cant_Horas"], m["Cant_Alumnos"]))
        materiasTabla=self.materias
        aulasDosModulos=len(self.fran.dia.aulas)
        aulasTresModulos=len(self.fran.dia.aulas)
        flag=True
        for x in self.materias:
            aleatorioMateria=random.randrange(0, len(materiasTabla))
            modulo=self.resolucionHoras(materiasTabla[aleatorioMateria], flag)
            aleatorioAula= random.randrange(0, len(self.fran.dia.aulas))
            disponibilidadDosModulos=self.fran.dia.aulas[aleatorioAula].aceptaDosModulos
            disponibilidadTresModulos=self.fran.dia.aulas[aleatorioAula].aceptaTresModulos
            disponibilidadHora=self.fran.dia.aulas[aleatorioAula].disponibilidad()
            if modulo==2:
                while disponibilidadDosModulos==False:
                    aleatorioAula= random.randrange(0, len(self.fran.dia.aulas))
                    disponibilidadDosModulos=self.fran.dia.aulas[aleatorioAula].aceptaDosModulos
                    disponibilidadHora=self.fran.dia.aulas[aleatorioAula].disponibilidad()
                    if aulasDosModulos==0:
                        self.materiasNoAsignadasDosModulos.append(materiasTabla[aleatorioMateria])
                        break
            else:
                while disponibilidadTresModulos==False:
                    aleatorioAula= random.randrange(0, len(self.fran.dia.aulas))
                    disponibilidadTresModulos=self.fran.dia.aulas[aleatorioAula].aceptaTresModulos
                    disponibilidadHora=self.fran.dia.aulas[aleatorioAula].disponibilidad()
                    if aulasTresModulos==0:
                        self.materiasNoAsignadasTresModulos.append(materiasTabla[aleatorioMateria])
                        break
            
            self.asignacion(disponibilidadHora, modulo, aleatorioAula, materiasTabla[aleatorioMateria])
            materiasTabla.pop(aleatorioMateria)
    
    def resolucionHoras(self, mt, flag):
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

    def asignacion(self, disponibilidad, modulo, aleatorioAula, materia):
        global aulasDosModulos
        global aulasTresModulos
        if modulo==2:
            if disponibilidad==time(7, 30):
                self.fran.dia.aulas[aleatorioAula].horas[0].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[0].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[1].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[1].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[2].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[2].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[3].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[3].materia=materia
                self.fran.dia.aulas[aleatorioAula].aceptaDosModulos=False
                aulasDosModulos = aulasDosModulos - 1
            elif disponibilidad==time(10, 30):
                self.fran.dia.aulas[aleatorioAula].horas[6].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[6].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[7].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[7].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[8].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[8].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[9].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[9].materia=materia
                self.fran.dia.aulas[aleatorioAula].aceptaDosModulos=False
                aulasDosModulos = aulasDosModulos - 1
        elif modulo==3:

            if disponibilidad==time(7, 30):
                self.fran.dia.aulas[aleatorioAula].horas[0].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[0].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[1].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[1].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[2].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[2].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[3].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[3].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[4].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[4].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[5].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[5].materia=materia
                self.fran.dia.aulas[aleatorioAula].aceptaTresModulos=False
                aulasTresModulos = aulasTresModulos - 1

            elif disponibilidad==time(9, 30):
                self.fran.dia.aulas[aleatorioAula].horas[4].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[4].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[5].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[5].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[6].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[6].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[7].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[7].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[8].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[8].materia=materia
                self.fran.dia.aulas[aleatorioAula].horas[9].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[9].materia=materia
                self.fran.dia.aulas[aleatorioAula].aceptaTresModulos=False
                self.fran.dia.aulas[aleatorioAula].aceptaDosModulos=False
                aulasTresModulos = aulasTresModulos - 1

    def elegirFranja(self, franja, materia):
        if franja=="Mañana":
            return materia.find({"Año":1})
        elif franja=="Tarde":
            return materia.find({"Año":{"$in":[2, 4]}})
        else:
            return materia.find({"Año":{"$in":[3, 5]}})
        
