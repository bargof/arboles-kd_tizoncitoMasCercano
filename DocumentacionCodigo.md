# Organización de los archivos:
## taquerias.json: 
Este archivo contiene, en formato JSON, los datos de 18 sucursales de la cadena de tacos El Tizoncito, 
dentro de las cuales se incluyen las coordenadas geográficas: latitud y lognitud.

## Prueba.py:
Clase principal ejecutable. En ella se extrae la información del archivo json en un diccionario para crear los objetos
que conformarán el árbol; serán de clase Taqueria. 

## ArbolKD.py:
Contiene todas las clases utilizadas para la ejecución en el siguiente orden:
1. **Util:** Contiene úncicamente una implementación de un método de ordenamiento por selección directa, el cual recibe como parámetro la dimensión que se alterna en cada nivel del árbol. La clase se definió para métodos auxiliares que no forman parte de otra clase.
2. **Taqueria:** Tiene como atributos los datos que contiene el json sobre las taquerías: colonia como nombre, latitud, longitud y dirección. Clase atómica de los objetos principales con los que trabajamos.
3. 
