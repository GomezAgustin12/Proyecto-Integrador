import numpy as np
import pandas as pd

class Aula:
    def __init__(self, codigo, piso, capacidad, descripcion):
        self.codigo=codigo
        self.piso=piso
        self.capacidad=capacidad
        self.descripcion=descripcion