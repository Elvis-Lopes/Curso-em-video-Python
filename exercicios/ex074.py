from random import randint
numList = []
for i in range(0, 5):
    numList.append(randint(0, 5))
numTupla = tuple(numList)
print(numTupla)
print(f'O menor valor da tupla é: {sorted(numTupla)[0]}')
print(f'O maior valor da tupla é {sorted(numTupla)[4]}')
