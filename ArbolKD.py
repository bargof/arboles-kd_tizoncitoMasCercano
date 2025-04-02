'''
@author Bargof 

30/03/2025
Definición del árbol k-d balanceado.
'''    
import math
from ClasesUtiles import Util, Taqueria 

class NodoKD: 
    def __init__(self, taqueria, dimension):
        self.taqueria = taqueria
        self.dimension = dimension # 0 (latitud) o 1 (longitud)
        self.hijo_izq = None
        self.hijo_der = None

class ArbolKD: 
    def __init__(self):
        self.raiz = None
    
    def insertar(self, nombre_colonia, direccion, latitud, longitud):
        if not self.raiz: 
            taqueria = Taqueria(nombre_colonia, direccion, latitud, longitud)
            self.raiz = NodoKD(taqueria, 0)
        else: 
            self.insertor_recursivo([taqueria], self.raiz, 0)

    def insertar_varios(self, taquerias):
        self.raiz = self.insertor_recursivo(taquerias, None, 0)

    def insertor_recursivo(self, taquerias, nodo, dimension):
        if not taquerias: 
            return nodo
        # se ordena según dimension actual (latitud: 0 o longitud: 1)
        taquerias = Util.seleccion_directa(taquerias, dimension)
        # se calcula la mediana
        pos_mediana = len(taquerias) // 2
        taqueria_mediana = taquerias[pos_mediana]
        if nodo is None: 
            nodo = NodoKD(taqueria_mediana, dimension)
        taquerias_menores = taquerias[:pos_mediana]
        taquerias_mayores = taquerias[pos_mediana + 1:]
        dimension_siguiente = 1 - dimension
        nodo.hijo_izq = self.insertor_recursivo(taquerias_menores, nodo.hijo_izq, dimension_siguiente)
        nodo.hijo_der = self.insertor_recursivo(taquerias_mayores, nodo.hijo_der, dimension_siguiente)
        return nodo
    
    def buscar(self, nodo, taqueria):
        if nodo is None:
            return None
        if taqueria.latitud == nodo.taqueria.latitud and taqueria.longitud == nodo.taqueria.longitud:
            return nodo.taqueria
        if (nodo.dimension == 0 and taqueria.latitud < nodo.taqueria.latitud) or (nodo.dimension == 1 and taqueria.longitud < nodo.taqueria.longitud):
            return self.buscar(nodo.hijo_izq, taqueria) 
        else:
            return self.buscar(nodo.hijo_der, taqueria)
        
    def eliminar(self, nodo, taqueria):
        if nodo is None:
            return nodo
        if taqueria.latitud == nodo.taqueria.latitud and taqueria.longitud == nodo.taqueria.longitud:
            # Si no tiene hijos
            if nodo.hijo_izq is None and nodo.hijo_der is None:
                return None
            # Si tiene un hijo
            if nodo.hijo_izq is None:
                return nodo.hijo_der  
            if nodo.hijo_der is None:
                return nodo.hijo_izq 
            # Si tiene dos hijos
            min_node = self._buscar_min(nodo.hijo_der, nodo.dimension)
            nodo.taqueria = min_node.taqueria 
            nodo.hijo_der = self.eliminar(nodo.hijo_der, min_node.taqueria)  
            return nodo
        if (nodo.dimension == 0 and taqueria.latitud < nodo.taqueria.latitud) or (nodo.dimension == 1 and taqueria.longitud < nodo.taqueria.longitud):
            nodo.hijo_izq = self.eliminar(nodo.hijo_izq, taqueria)
        else:
            nodo.hijo_der = self.eliminar(nodo.hijo_der, taqueria)
        return nodo

    def _buscar_min(self, nodo, dimension):
        if nodo is None:
            return None
        if dimension == 0:
            if nodo.hijo_izq is None:
                return nodo
            return self._buscar_min(nodo.hijo_izq, dimension)
        elif dimension == 1:
            if nodo.hijo_der is None:
                return nodo
            return self._buscar_min(nodo.hijo_der, dimension)


    def distancia_euclidiana(self, taqueria1, taqueria2):
        return math.sqrt((taqueria1.latitud - taqueria2.latitud) ** 2 + (taqueria1.longitud - taqueria2.longitud) ** 2)

    def k_nearest_neighbors(self, nodo, punto_consulta, k, mejores_vecinos=None):
        if mejores_vecinos is None:
            mejores_vecinos = []
        if nodo is None:
            return mejores_vecinos
        distancia = self.distancia_euclidiana(nodo.taqueria, punto_consulta)
        mejores_vecinos.append((distancia, nodo.taqueria))
        mejores_vecinos.sort(key=lambda x: x[0])
        if len(mejores_vecinos) > k:
            mejores_vecinos.pop()
        # Calcular la distancia al punto de particion segun la dimension
        if nodo.dimension == 0:
            delta = abs(punto_consulta.latitud - nodo.taqueria.latitud)
        elif nodo.dimension == 1:
            delta = abs(punto_consulta.longitud - nodo.taqueria.longitud)
        if (nodo.dimension == 0 and punto_consulta.latitud < nodo.taqueria.latitud) or (nodo.dimension == 1 and punto_consulta.longitud < nodo.taqueria.longitud):
            # Vamos al subarbol izquierdo 
            mejores_vecinos = self.k_nearest_neighbors(nodo.hijo_izq, punto_consulta, k, mejores_vecinos)
            # Revisamos si es necesario explorar el derecho
            if len(mejores_vecinos) < k or delta < mejores_vecinos[-1][0]:
                mejores_vecinos = self.k_nearest_neighbors(nodo.hijo_der, punto_consulta, k, mejores_vecinos)
        else:
            # Vamos al derecho 
            mejores_vecinos = self.k_nearest_neighbors(nodo.hijo_der, punto_consulta, k, mejores_vecinos)
            # Revisamos si es necesario explorar el izquierdo
            if len(mejores_vecinos) < k or delta < mejores_vecinos[-1][0]:
                mejores_vecinos = self.k_nearest_neighbors(nodo.hijo_izq, punto_consulta, k, mejores_vecinos)
        return mejores_vecinos


    def obtener_k_vecinos_mas_cercanos(self, punto_consulta, k):
        vecinos = self.k_nearest_neighbors(self.raiz, punto_consulta, k)
        return [vecino[1] for vecino in vecinos]
