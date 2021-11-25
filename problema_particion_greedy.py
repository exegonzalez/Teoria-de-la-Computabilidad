#!/usr/bin/env python

import random, time

def greedy(list_):
    """
    Divide los elementos en dos subconjuntos aproximadamente iguales con un algoritmo "codicioso". 
    Ordena los elementos y luego los asigna al subconjunto más pequeño.

    .. advertencia::
        Un algoritmo "codicioso" puede no devolver la solución óptima.

    : parámetro list_: una lista de números positivos
    : tipo list_: list

    : return: diferencia mínima entre sumas de subconjuntos, lista de subconjuntos solución
    : tipo return: float, list
    """
    list_ = sorted(list_, reverse=True)
    diff = 0.
    subc1 = []
    subc2 = []
    for item in list_:
        if diff <= 0.:
            diff += item
            subc1.append(item)
        else:
            diff -= item
            subc2.append(item)

    return abs(diff), [subc1,subc2]

if __name__ == "__main__":
    # S = [1, 15, 29, 101, 261, 152, 11, 25, 13, 22, 51, 37, 12,1]

    S = []
    for i in range(0,10000):
        S.append(random.randint(0,1000))
    print('El conjunto es:',S)
    inicio = time.time()
    greedy(S)
    fin = time.time()
    print('Tiempo de ejecución: ', fin-inicio)