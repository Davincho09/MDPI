# Particle Swarm Optimization (PSO)

## Qué es?

Es un algoritmo inspirado en los emjabres de partículas, especialmente enfocado en la naturaleza. El PSO es un método de optimización basado en poblaciones donde cada posible solución ó partícula, se mueve en el espacio de búsqueda siguiendo dos influencias principales, su propia experiencia pasada, es decir la mejor solución que ha encontrado hasta ahora y la experiencia del grupo, la mejor solución encontrada por todo el enjambre. El movimiento de cada partícula se ajusta mediante velocidades y posiciones que dependen de estos factores, buscando balancear exploración y explotación.

## Un ejemplo conceptual?

Si tomamos un emjambre de **Abejas**, es posible determinar su algoritmo de partículas con su comportamiento natural, se tiene un emjambre de ellas, vuelan aleatoriamente a varios puntos de una zona en especifico, si una de ellas encuentra una flor, esta recuerda la ubicación de donde se encuentra, las abejas son capaces de comunicarse entre sí, y tienen la experiencia pasada, tanto de la abeja invidual como del enjambre completo, tendrán en cuenta los lugares que exploraron en función a las **Flores que ya encontraron**.


## Un ejemplo matemático?

es posible tomar una función cualquiera y aplicar un resultado invididual y resultado grupal.

En este ejemplo, un enjambre de abejas busca las flores más ricas en néctar dentro de un campo. El campo está representado por una función de optimización:

𝑓(𝑥,𝑦)=𝑥^2+𝑦^2

El mínimo global de esta función está en (0,0), que equivale a la flor con más néctar.

Cada abeja corresponde a una partícula del algoritmo PSO.

Cada abeja  𝑖 tiene:

Una posición en el campo:

𝑥⃗𝑖=(𝑥𝑖,𝑦𝑖)xit
	​
Una velocidad de vuelo:
𝑣⃗𝑖𝑡vit	​
Cada abeja recuerda su mejor flor personal encontrada:
𝑝⃗𝑖𝑡pit
	​
 
La mejor flor global encontrada por el enjambre:

𝑔⃗𝑡gt

Las abejas vuelan al azar al inicio (exploración del campo), cada una recuerda la mejor flor que halló (memoria individual), comparten información y se van moviendo hacia la flor más rica (memoria colectiva) Finalmente el enjambre converge al mínimo global , la flor con mayor néctar.
