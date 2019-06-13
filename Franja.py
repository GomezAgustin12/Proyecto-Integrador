import numpy as np
import pandas as pd
from datetime import datetime, date, time, timedelta

import Dia
Dia=Dia.Dia

class Franja:
    def __init__(self, franja):
        self.nombre=franja
        self.asignarHorario()

    def asignarHorario(self):
        if self.nombre=="Mañana":
            self.inicio=time(8)
            self.fin=time(12, 30)
        elif self.nombre=="Tarde":
            self.inicio=time(12, 30)
            self.fin=time(12, 30)
        else:
            self.inicio=time(18)
            self.fin=time(23)


    def agregarDia(self, dia, franja):
        self.dia= Dia(dia, franja)

