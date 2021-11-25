# """
# El Problema consiste en decidir si, dado un multiconjunto de números enteros, puede este ser particionado en dos "mitades" 
# tal que sumando los elementos de cada una, ambas den como resultado la misma suma. Dado un multiconjunto S de enteros: 
# ¿existe alguna forma de partir S en dos subconjuntos S1 y S2, tal que la suma de los elementos en S1 sea igual que la suma 
# de los elementos en S2?
# """
import random, time, itertools, copy

def dividirConjunto(S):

	total = sum(S)
	mitad = total//2
	subconjuntos = []
	inicio = time.time()

	if (total % 2 == 0):
		for L in range(0, len(S)+1):
			for subset in itertools.combinations(S, L):
				if (sum(subset)==mitad):
					A = S.copy()
					for element in subset:
						A.remove(element)
					subconjuntos.append([list(subset), A])
		fin = time.time()

		if len(subconjuntos)>0:
			print('Existen dos subconjuntos que sumen lo mismo')
			for i in range(0, len(subconjuntos)//2):
				print(f'Solución {i} - Subconjunto A:{subconjuntos[i][0]} - Subconjunto B:{subconjuntos[i][1]}')
				
		else:
			print('No existen dos subconjuntos que sumen lo mismo')
		return inicio, fin
	else:
		fin = time.time()
		print('La suma del conjunto no se puede dividir a la mitad')
		return inicio, fin


if __name__ == '__main__':

	# Entrada: un conjunto de números enteros
	# S = [7, 3, 2, 1, 5, 4, 8]
	# S = [3,1,1,2,2,1]
	S = []
	for i in range(0,10):
		S.append(random.randint(-1000, 1000))
	print('El conjunto es:',S)
	inicio, fin = dividirConjunto(S)
	print('Tiempo de ejecución: ', fin-inicio)



