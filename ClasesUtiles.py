'''
@author Bargof

Clases utiles y atómicas (de más bajo nivel jerárquico).
'''
import math 

class Util: 
    # seleccion directa, ordenando por dimension (latitud o longitud de la taquería)
    def seleccion_directa(taquerias, dimension):
        n = len(taquerias)

        for i in range(n):
            pos_min = i
            for j in range(i + 1, n):
                if dimension == 0:
                    if (taquerias[j].latitud < taquerias[pos_min].latitud):
                        pos_min = j
                elif dimension == 1:
                    if (taquerias[j].longitud < taquerias[pos_min].longitud):
                        pos_min = j
            taquerias[i], taquerias[pos_min] = taquerias[pos_min], taquerias[i]
        return taquerias


class Taqueria: 
    def __init__(self, nombre_colonia, direccion, latitud, longitud):
        self.nombre_colonia = nombre_colonia
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud

    def get_direccion(self):
        return self.direccion
