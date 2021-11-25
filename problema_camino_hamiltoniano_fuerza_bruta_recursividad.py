import random, time, string

def generarAristas(N):
	aristas = []

	for i in range(0,N):
		for j in range(0,N):
			if i!=j and (random.randint(0, 100) >= 80):
				if (string.ascii_letters[i], string.ascii_letters[j]) not in aristas:
					aristas.append((string.ascii_letters[j],string.ascii_letters[i]))

	return aristas


def generarGrafo(aristas):
    dic = {}

    for (orig, dest) in aristas:
        if(orig in dic.keys()):
            dic[orig] = dic[orig]+str(dest)
            if(dest in dic.keys()):
                dic[dest] = dic[dest]+str(orig)
            else:
                dic[dest] = str(orig)
        else:
            dic[orig] = str(dest)
            if(dest in dic.keys()):
                dic[dest] = dic[dest]+str(orig)
            else:
                dic[dest] = str(orig)

    return dic


def hamiltonians(G, vis = []):
    if not vis:
        for n in G:
            for p in hamiltonians(G, [n]):
                yield p
    else:
        dests = set(G[vis[-1]]) - set(vis)
        if not dests and len(vis) == len(G):
            yield vis
        for n in dests:
            for p in hamiltonians(G, vis + [n]):
                yield p
                
N = 10
x = generarAristas(N)
g = generarGrafo(x)

print('El grafo es:', g)
inicio = time.time()
list(hamiltonians(g))
fin = time.time()

print('Tiempo de ejecución: ', fin-inicio)