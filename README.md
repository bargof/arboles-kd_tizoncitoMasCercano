# Árboles k-d (k-dimensionales)

**Definición:** 
Un árbol k-d es una estructura de datos que organiza puntos en espacios multidimensionales.
Cada nodo del árbol representa un punto que divide el espacio en dos partes alternando
dimensiones en cada nivel. Esto facilita búsquedas rápidas de puntos en varias dimensiones.

**Casos de uso:**
* Sistemas de Información Geográfica (GIS), sistemas GPS
* Detección de colisiones en videojuegos y gráficos 3D
* Algoritmos de clasificación y recomendación (KNN) en aprendizaje automático

**Árbol k-d balanceado vs no balanceado**
* Balanceado: Usa medianas para dividir, garantizando una altura aproximada de O(log n),
lo que optimiza las búsquedas.
* No balanceado: Se obtiene al insertar puntos secuencialmente ordenados, resultando en
una altura O(n), menos eficiente.

## Estructura
**Construcción:** (usando medianas para balancearlo)
1. Escoger dimensión alternando en cada nivel.
2. Calcular la mediana en la dimensión elegida.
3. Dividir puntos y aplicar recursivamente para los subárboles resultantes.
Tiempo: O(n log n) | Espacio: O(n)


**Ejemplo simple (2D):**
1. Supongamos los puntos: (2,3), (5,4), (9,6), (4,7), (8,1), (7,2)
2. Se elige el eje X para la raíz y la mediana es (7,2).
3. A la izquierda del 7 (X<7) están los puntos (2,3), (5,4), (4,7).
4.  En el siguiente nivel, con eje Y, la mediana es (5,4), dividiendo en (2,3) abajo y (4,7)
arriba.
5. A la derecha del 7 (X≥7) está el punto (9,6) y (8,1); con eje Y la mediana es (9,6),
dejando (8,1) abajo.


## Algoritmos
### Inserción
1. Comenzar desde la raíz.
2. Alternar la dimensión de comparación según el nivel actual.
3. Comparar el nuevo punto con el punto actual, moverse al subárbol izquierdo o derecho.
4. Continuar hasta encontrar una posición vacía; insertar el nuevo punto.
* Tiempo: O(log n) promedio, O(n) peor caso | Espacio: O(1)
### Búsqueda
1. Comenzar desde la raíz.
2. Comparar el punto buscado con el punto actual.
3. Si coinciden todas las dimensiones, termina exitosamente.
4. Si no, decidir el subárbol izquierdo o derecho según la dimensión actual.
* Tiempo: O(log n) promedio, O(n) peor caso | Espacio: O(1)
### Eliminación
1. Encontrar el nodo con el punto a eliminar.
2. Si es hoja, eliminar directamente.
3. Si tiene un solo hijo, reemplazarlo directamente con el hijo.
4. Si tiene dos hijos:
   1. Encontrar el mínimo en la misma dimensión del subárbol derecho.
   2. Copiar ese punto al nodo actual y eliminar el nodo mínimo encontrado (que tendrá 0 o 1 hijo).
* Tiempo: O(log n) promedio, O(n) peor caso | Espacio: O(1)
### Algoritmo KNN (vecinos más cercanos)
1. Descender desde la raíz hasta una hoja usando comparaciones normales.
2. Retroceder y registrar los K vecinos más cercanos encontrados.
3. Para cada nodo durante retroceso:
◦ Actualizar vecinos más cercanos si es necesario.
◦ Determinar si se explora el otro subárbol comparando la distancia al plano de
división con la distancia al K-ésimo vecino encontrado.
4. Continuar hasta regresar a la raíz.
* Tiempo: O(log n + k) promedio, O(n) peor caso | Espacio: O(k)

## Bibliografía 
* Bentley, J. L. (1975). Communications of the ACM, 18(9), 509-517.
* Friedman, J. H., et al. (1977). ACM Transactions on Mathematical Software, 3(3),
209-226.
* de Berg, M., et al. (2008). Computational Geometry: Algorithms and Applications (3ra
ed.). Springer.
