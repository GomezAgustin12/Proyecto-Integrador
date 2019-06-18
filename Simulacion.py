# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import pandas as pd
import random
from datetime import datetime, date, time, timedelta

import sys

import Franja 
Franja=Franja.Franja
import Materias
Materia= Materias.Materia

aulasDosModulos=0
aulasTresModulos=0

from PyQt5 import QtCore, QtGui, QtWidgets

class Simulacion(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 350)
        MainWindow.setMinimumSize(QtCore.QSize(554, 350))
        MainWindow.setMaximumSize(QtCore.QSize(554, 350))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.506, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(170, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_simular = QtWidgets.QPushButton(self.centralwidget)
        self.boton_simular.setGeometry(QtCore.QRect(230, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.boton_simular.setFont(font)
        self.boton_simular.setStyleSheet("color: rgb(255, 255, 255);")
        self.boton_simular.setObjectName("boton_simular")
        self.franjaHoraria = QtWidgets.QComboBox(self.centralwidget)
        self.franjaHoraria.setGeometry(QtCore.QRect(230, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.franjaHoraria.setFont(font)
        self.franjaHoraria.setStyleSheet("")
        self.franjaHoraria.setObjectName("franjaHoraria")
        self.franjaHoraria.addItem("")
        self.franjaHoraria.addItem("")
        self.franjaHoraria.addItem("")
        self.dia = QtWidgets.QComboBox(self.centralwidget)
        self.dia.setGeometry(QtCore.QRect(230, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dia.setFont(font)
        self.dia.setObjectName("dia")
        self.dia.addItem("")
        self.dia.addItem("")
        self.dia.addItem("")
        self.dia.addItem("")
        self.dia.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 120, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(250,0, 0, 0);\n"
        "color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(250,0, 0, 0);\n"
        "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(255, 0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.fondo = QtWidgets.QLabel(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 554, 350))
        self.fondo.setStyleSheet("border-image: url(:/imagenes/fondo.jpg);")
        self.fondo.setText("")
        self.fondo.setObjectName("fondo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 30, 61, 41))
        self.label_4.setStyleSheet("border-image: url(:/imagenes/Isotipo-CMYK-300-Color.png);\n"
        "background-color: rgb(255, 0, 0, 0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.fondo.raise_()
        self.boton_simular.raise_()
        self.franjaHoraria.raise_()
        self.dia.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.boton_simular.clicked.connect(self.operacion)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SADA"))
        self.boton_simular.setText(_translate("MainWindow", "Simular"))
        self.franjaHoraria.setCurrentText(_translate("MainWindow", "Mañana"))
        self.franjaHoraria.setItemText(0, _translate("MainWindow", "Mañana"))
        self.franjaHoraria.setItemText(1, _translate("MainWindow", "Tarde"))
        self.franjaHoraria.setItemText(2, _translate("MainWindow", "Noche"))
        self.dia.setItemText(0, _translate("MainWindow", "Lunes"))
        self.dia.setItemText(1, _translate("MainWindow", "Martes"))
        self.dia.setItemText(2, _translate("MainWindow", "Miercoles"))
        self.dia.setItemText(3, _translate("MainWindow", "Jueves"))
        self.dia.setItemText(4, _translate("MainWindow", "Viernes"))
        self.label.setText(_translate("MainWindow", "Seleccione franja horaria"))
        self.label_2.setText(_translate("MainWindow", "Seleccione día"))
        self.label_3.setText(_translate("MainWindow", "SADA"))

#-------------------------------------HASTA ACA LLEGA LA INTERFACE--------------------------------------------


#-------------------------------------ACA COMIENZA EL CODIGO O ALGO ASI---------------------------------------
    def operacion(self):
        franja = self.franjaHoraria.currentText()
        dia = self.dia.currentText()
        sim= Simulacion()
        sim.simulacionFranjaDia(franja,dia)
        col=["Aulas"]
        tabla=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        i=0
        for a in sim.fran.dia.aulas[0].horas:
            col.append(a.hora)
        for x in sim.fran.dia.aulas:
            tabla[i].append(x.descripcion)
            for y in x.horas:
                tabla[i].append(y.asignado)
            i=i+1
        df=pd.DataFrame(tabla, columns=col)
        writer = ExcelWriter('NuevaTabla.xlsx')
        df.to_excel(writer,'Salida', index=False)
        writer.save()
        print("Fin")


    def simulacionFranjaDia(self, franja, dia):
        global aulasDosModulos
        global aulasTresModulos
        self.materiasNoAsignadasTresModulos=[]
        self.materias=[]
        self.materiasNoAsignadasDosModulos=[]
        self.fran=Franja(franja, dia)
        excelMateria=pd.read_excel("E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Tablas.xlsx", "Materia")
        if franja=="Mañana":
            i=0
            for m in excelMateria.Año:    
                    if excelMateria.Año[i] == 1:
                        self.materias.append(Materia(excelMateria.CodigoMateria[i], excelMateria.Facultad[i], excelMateria.Carrera[i], excelMateria.Nombre[i], excelMateria.Año[i], excelMateria.Semestre[i], excelMateria.CantHs[i], excelMateria.CantAlumnos[i]))
                    i=i+1

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

                
                self.asignacion(disponibilidadHora, modulo, aleatorioAula)
                materiasTabla.pop(aleatorioMateria)
                


        elif franja=="Tarde":
            i=0
            for m in excelMateria.Año:    
                    if excelMateria.Año[i] == 1:
                        self.materias.append(Materia(excelMateria.CodigoMateria[i], excelMateria.Facultad[i], excelMateria.Carrera[i], excelMateria.Nombre[i], excelMateria.Año[i], excelMateria.Semestre[i], excelMateria.CantHs[i], excelMateria.CantAlumnos[i]))
                    i=i+1

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

                
                self.asignacion(disponibilidadHora, modulo, aleatorioAula)
                materiasTabla.pop(aleatorioMateria)
        else:
            i=0
            for m in excelMateria.Año:    
                    if excelMateria.Año[i] == 1:
                        self.materias.append(Materia(excelMateria.CodigoMateria[i], excelMateria.Facultad[i], excelMateria.Carrera[i], excelMateria.Nombre[i], excelMateria.Año[i], excelMateria.Semestre[i], excelMateria.CantHs[i], excelMateria.CantAlumnos[i]))
                    i=i+1

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

                
                self.asignacion(disponibilidadHora, modulo, aleatorioAula)
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

    def asignacion(self, disponibilidad, modulo, aleatorioAula):
        global aulasDosModulos
        global aulasTresModulos
        if modulo==2:
            if disponibilidad==time(7, 30):
                self.fran.dia.aulas[aleatorioAula].horas[0].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[1].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[2].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[3].asignado=True
                self.fran.dia.aulas[aleatorioAula].aceptaDosModulos=False
                aulasDosModulos = aulasDosModulos - 1
            elif disponibilidad==time(10, 30):
                self.fran.dia.aulas[aleatorioAula].horas[6].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[7].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[8].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[9].asignado=True
                self.fran.dia.aulas[aleatorioAula].aceptaDosModulos=False
                aulasDosModulos = aulasDosModulos - 1
        elif modulo==3:

            if disponibilidad==time(7, 30):
                self.fran.dia.aulas[aleatorioAula].horas[0].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[1].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[2].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[3].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[4].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[5].asignado=True
                self.fran.dia.aulas[aleatorioAula].aceptaTresModulos=False
                aulasTresModulos = aulasTresModulos - 1

            elif disponibilidad==time(9, 30):
                self.fran.dia.aulas[aleatorioAula].horas[4].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[5].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[6].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[7].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[8].asignado=True
                self.fran.dia.aulas[aleatorioAula].horas[9].asignado=True
                self.fran.dia.aulas[aleatorioAula].aceptaTresModulos=False
                self.fran.dia.aulas[aleatorioAula].aceptaDosModulos=False
                aulasTresModulos = aulasTresModulos - 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Simulacion()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

