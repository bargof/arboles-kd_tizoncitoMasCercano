'''
@author Fernando Barrios
@author sofia Bonilla

Preuba de: 
Implementación de árbol k-d balanceado para encontrar El Tizoncito (taquería) más cercano a algún punto.
'''
import json
from ArbolKd import ArbolKD, Taqueria 

# Carga el JSON en un diccionario
with open('taquerias.json', 'r', encoding='utf-8') as file:
    datos_json = json.load(file)

lista_taquerias = []
for item in datos_json:
    taqueria = Taqueria(
        item["colonia"],
        item["direccion"],
        item["latitud"],
        item["longitud"]
    )
    lista_taquerias.append(taqueria)
arbol = ArbolKD()
arbol.insertar_varios(lista_taquerias)

# KNN para taquería mas cercana a:
itam = Taqueria("ITAM", "Rio hondo 1", 19.345324, -99.200981)
vecinos_cercanos = arbol.obtener_k_vecinos_mas_cercanos(itam, 1)
print(f"\nTizoncito más cercano: {vecinos_cercanos[0].direccion}\n")