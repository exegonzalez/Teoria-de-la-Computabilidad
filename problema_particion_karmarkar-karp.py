#!/usr/bin/env python

import random, time
from bisect import insort

def KK(list_):
    """
    Divide los elementos en dos subconjuntos aproximadamente iguales con el algoritmo Karmarkar-Karp, 
    también conocido como "método de la mínima diferencia".

    .. advertencia::
        Es posible que este algoritmo no devuelva la solución óptima.

    : parámetro list_: una lista de números positivos
    : tipo lista_: list

    : return: diferencia mínima entre sumas de subconjuntos
    : tipo return: float
    """
    list_ = sorted(list_)
    while len(list_) > 1:
        diff = list_.pop() - list_.pop()
        insort(list_, diff)

    return list_[0]


if __name__ == "__main__":
    # example_list = [1, 15, 29, 101, 261, 152, 11, 25, 13, 22, 51, 37, 12,1]

    S = []
    for i in range(0,10000):
        S.append(random.randint(0,1000))
    print('El conjunto es:',S)
    inicio = time.time()
    KK(S)
    fin = time.time()
    print('Tiempo de ejecución: ', fin-inicio)