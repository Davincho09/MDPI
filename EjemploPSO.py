import numpy as np
import matplotlib.pyplot as plt

def nectar(position):
    x, y = position
    return x**2 + y**2  


abejas = 20       
dim = 2          
iteraciones = 40
w = 0.7           
c1 = 1.5          
c2 = 1.5         

# --- Inicialización aleatoria del enjambre ---
posiciones = np.random.uniform(-10, 10, (abejas, dim))  
velocidades = np.random.uniform(-1, 1, (abejas, dim))   

# Mejor posición individual
pbest = posiciones.copy()
pbest_valores = np.array([nectar(p) for p in posiciones])

# Mejor flor global encontrada
gbest = pbest[np.argmin(pbest_valores)]


historia = []
for t in range(iteraciones):
    for i in range(abejas):
        valor = nectar(posiciones[i])
        
        if valor < pbest_valores[i]:
            pbest[i] = posiciones[i]
            pbest_valores[i] = valor
    
    gbest = pbest[np.argmin(pbest_valores)]
    historia.append(nectar(gbest))
    
    for i in range(abejas):
        r1, r2 = np.random.rand(), np.random.rand()
        velocidades[i] = (w*velocidades[i] 
                          + c1*r1*(pbest[i] - posiciones[i]) 
                          + c2*r2*(gbest - posiciones[i]))
        posiciones[i] += velocidades[i]

print("Mejor flor encontrada en:", gbest)
print("Cantidad de néctar:", nectar(gbest))

# --- Gráfico de convergencia ---
plt.plot(historia, marker="o", color="purple")
plt.title("Enjambre de abejas buscando flores (PSO)")
plt.xlabel("Iteración")
plt.ylabel("Néctar encontrado (valor de fitness)")
plt.grid()
plt.show()
