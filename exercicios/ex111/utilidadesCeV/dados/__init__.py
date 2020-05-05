from numpy.core.defchararray import isnumeric
from exercicios.ex111.utilidadesCeV import moeda

def leiaDinheiro (valor):
    while True:
        if isnumeric(valor):
            break
        else:
            print('Digite um valor valido')
