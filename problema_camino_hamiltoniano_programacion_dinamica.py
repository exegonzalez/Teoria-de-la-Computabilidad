import random, time

def generarGrafoAleatorio(N):
    grafo = [[0 for col in range(N)] for row in range(N)]

    for i in range(0,N):
        for j in range(0,N):
            if i!=j and (random.randint(0,100)>=80):
                grafo[i][j] = 1
                grafo[j][i] = 1

    return grafo


# Función para comprobar si existe una ruta hamiltoniana o no
def Hamiltonian_path(adj, N):
     
    dp = [[False for i in range(1 << N)]
                 for j in range(N)]

    # Establece todos los dp[i][(1 << i)] en True
    for i in range(N):
        dp[i][1 << i] = True
 
    # Itera sobre cada subconjunto de nodos
    for i in range(1 << N):
        for j in range(N):
 
            # Si los nodos están incluidos en el subconjunto actual
            if ((i & (1 << j)) != 0):
 
                # Encuentra K, vecino de j también presente en el subconjunto actual
                for k in range(N):
                    if ((i & (1 << k)) != 0 and
                             adj[k][j] == 1 and
                                     j != k and
                          dp[k][i ^ (1 << j)]):
                         
                        # Actualiza dp[j][i] a True
                        dp[j][i] = True
                        break
     
    # Recorre los vértices
    for i in range(N):
 
        # Existe el camino hamiltoniano
        if (dp[i][(1 << N) - 1]):
            return True
 
    # Caso contrario, devuelve falso
    return False
 
# G = [[ 0, 1, 1, 1, 0 ],
#      [ 1, 0, 1, 0, 1 ],
#      [ 1, 1, 0, 1, 1 ],
#      [ 1, 0, 1, 0, 0 ],
#      [ 0, 1, 1, 0, 0 ]]
 
N = 24
L = 0
g = generarGrafoAleatorio(N)

print('El grafo es:', g)
inicio = time.time()
x = Hamiltonian_path(g, N)
fin = time.time()
if (x):
    print("YES")
else:
    print("NO")
    
print('Tiempo de ejecución: ', fin-inicio)