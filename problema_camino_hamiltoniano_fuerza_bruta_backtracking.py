"""
# En teoría de grafos, un camino hamiltoniano en un grafo es un camino (es decir, una sucesión de aristas adyacentes), 
# que visita todos los vértices del grafo una sola vez. Si además el primer y último vértice visitado coincide, 
# el camino es un ciclo hamiltoniano.
"""
import time, random

# clase para crear objetos Grafo.
class Grafo:

	# Constructor
	def __init__(self, aristas, N):

		# Lista de listas para representar una lista de adyacencias
		self.listaAdy = [[] for _ in range(N)]

		# Agregar aristas al grafo no dirigido
		for (orig, dest) in aristas:
			self.listaAdy[orig].append(dest)
			self.listaAdy[dest].append(orig)


def generarGrafoAleatorio(N):
	aristas = []

	for i in range(0,N):
		for j in range(0,N):
			if i!=j and (random.randint(0, 100) >= 80):
				if (i, j) not in aristas:
					aristas.append((j,i))

	return aristas


def mostrarCaminosHamiltonianos(g, v, visitados, camino, N):

	# Si se visitan todos los vértices, entonces existe el camino hamiltoniano
	if len(camino) == N:
		# Muestra el camino hamiltoniano
		# print(camino)
		return

	# Comprueba si cada arista que comienza desde el vértice 'v' conduce a una solución o no
	for w in g.listaAdy[v]:

		# Procesa solo los vértices no visitados ya que el camino hamiltoniano 
        # visita cada vértice exactamente una vez
		if not visitados[w]:
			visitados[w] = True
			camino.append(w)

			# Comprueba si agregar el vértice 'w' a la ruta conduce a la solución o no
			mostrarCaminosHamiltonianos(g, w, visitados, camino, N)

			# Retractarse
			visitados[w] = False
			camino.pop()


if __name__ == '__main__':

	# Número total de vértices en el gráfico
	N = 10

	# Entrada: un conjunto de vértices con sus aristas
	aristas = generarGrafoAleatorio(N)

	# Construye un grafo a partir de la entrada
	g = Grafo(aristas, N)
	print('El grafo es:', g.listaAdy)

	inicio = time.time()
	for i in range(0, N):
		# Agrega el vértice inicial al camino hamiltoniano
		camino = [i]
		
		# Crea una lista para controlar los vértices visitados
    	# Marca el vértice inicial como visitado
		visitados = [False] * N
		visitados[i] = True
		
		mostrarCaminosHamiltonianos(g, i, visitados, camino, N)
	fin = time.time()
	
	print('Tiempo de ejecución: ', fin-inicio)
