# Organización de los archivos:
## taquerias.json: 
Este archivo contiene, en formato JSON, los datos de 18 sucursales de la cadena de tacos El Tizoncito, 
dentro de las cuales se incluyen: [nombre_colonia, direccion, latitud, longitud].

## ClasesUtiles.py:
Clases utiles auxiliares y clases del nivel más bajo jerárquico.
* **Util**: Definición de métodos estaticos utiles.
  * Métodos: 
    | Método                                                 | Descripción                                                                                                       |
    |--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
    | +<ins>seleccion_directa</ins>(Taqueria, int): Taqueria | Implementación de ordenamiento por selección directa, con la diferencia que toma en cuenta la dimensión (dada en el parámetro de entrada) para ordenar según esta.<br>Los objetos de la clase Taqueria tienen dos dimensiones: latitud y longitud (0 y 1 respectivamente). |


## ArbolKD.py:
Clases Nodo y Arbol:
1. **NodoKD:** Nodo para el árbol k-d.
    * Atributos:
       | Atributo                       | Descripción                                                                              |
       |--------------------------------|------------------------------------------------------------------------------------------|
       | -taqueria: Taqueria            | Dato del nodo. Un objeto de la clase Taqueria.                                           |
       | -dimension: int                | Describe el nivel del árbol en el que se encuentra, alternadamente. Puede ser 0 o 1 (latitud o longitud respectivamente). |
       | -hijo_izq: NodoKD              | Apunta al subarbol izquierdo.                                                            |
       | -hijo_der: NodoK               | Apunta al subarbol derecho.                                                              |
       
    * Métodos:

     
2. **ArbolKD:** 

## Prueba.py:
Clase principal ejecutable. En ella se extrae la información del archivo json en un diccionario para crear los objetos
que conformarán el árbol; serán de clase Taqueria. 
