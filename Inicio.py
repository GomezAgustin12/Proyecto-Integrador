import numpy as np
import pandas as pd

import Carrera
Carrera=Carrera.Carrera
import Materias
Materia=Materias.Materia
import Facultad
Facultad=Facultad.Facultad


class Inicio:
    def __init__ (self, excel):
        self.ex=pd.read_excel(excel)

    def carga(self):
        banderaF=0
        banderaC=0
        banderaA=0

        i=0
        contF=0
        contC=0
        contA=0

        auxF=self.ex.Facultad[0]
        auxC=self.ex.Carrera[0]
        auxA=self.ex.Año[0]
        while self.ex.Facultad[i]:
        
#Carga Facultad
            if auxF==self.ex.Facultad[i] and banderaF == 0:
                objF.append(Facultad(auxF))
                print(objF[0].nombre)
                contF=contF+1
                banderaF=1
            elif auxF!=self.ex.Facultad[i] and banderaF == 1:
                banderaF=0
                auxF=self.ex.Facultad[i+1]
#Carga Carrera
            if auxC==self.ex.Carrera[i] and banderaC == 0:
                objF[contF-1].crearCarrera(auxC)
                print(" ", objF[contF-1].carreras[contC].nombre)
                contC=contC+1
                banderaC=1
            elif auxC!=self.ex.Carrera[i] and banderaC == 1:
                banderaC=0
                auxC=self.ex.Carrera[i+1]
#Carga Materia
            objF[contF-1].carreras[contC-1].crearMateria(self.ex.Materia[i], self.ex.Año[i])
            print("         ", objF[contF-1].carreras[contC-1].materias[i].nombre, "     ", objF[contF-1].carreras[contC-1].materias[i].semestre)
            i=i+1
            
objF=[]
inicio= Inicio("E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Materias.xlsx")
inicio.carga()
