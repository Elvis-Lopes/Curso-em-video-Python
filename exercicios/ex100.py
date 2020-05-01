from random import randint

def sortear(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 18))
def somarPar(lista):
    soma = 0
    for i in range(0, 5):
        if lista[i] % 2 == 0:
            soma += lista[i]
    print(f'a soma dos números é {soma}')


numeros = list()
sortear(numeros)
print(numeros)
somarPar(numeros)