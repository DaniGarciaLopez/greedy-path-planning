# Descripción del algortimo

El algoritmo greedy implementado utiliza una heurística basada en la aleatoriedad del sentido de giro para adaptarse a cualquier tipo de mapa. 
En el inicio se selecciona una dirección y se sigue hasta que se colisiona con un obstáculo.
Posteriormente se selecciona otra dirección, si no hay obstáculo y no es un camino visitado se sigue esa dirección hasta que vuelve a colisionar.
Cuando no hay camino libre, se vuelve al nodo anterior y se comprueba si tiene algúna dirección libre y si no, se sigue iterando en los nodos previos.

# Resultados

El algoritmo greedy resulta ser en general más rápido que el BFS en la mayoría de situaciones. 
Sin embargo, no suele encontrar el camino óptimo. Esto se hace especialmente evidente cuando los mapas son muy cuadrados y el algoritmo realiza caminos en forma de espiral. 
Para evitar eso, sería conveniente aplicar un algoritmo de búsqueda en nodos como Dijsktra o A* tras haber llegado a la meta para trazar el camino final.

# Extras
- Se ha realizado una interfaz gráfica para visualizar los mapas de forma cómoda en la terminal. El borrado de pantalla es compatible con windows y linux. La tasa de refresco se modifica con la variable "DISPLAY_TIME".
- La ruta final se representa en el mapa al encontrar la meta.
- Los mapas y los algoritmos se seleccionan mediante la terminal. Los puntos de inicio y final se cargan mediante un diccionario. Se evitan errores en la introducción de los números de selección.
- Se calcula el tiempo de cómputo de cada algoritmo. Este cálculo ignora las esperas realizadas para la visualización.
- Vídeo: https://youtu.be/eMjHF4yqs44

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/eMjHF4yqs44/0.jpg)](https://youtu.be/eMjHF4yqs44)
