# aula de importação de modulos
from math import sqrt, ceil
num = int(input('Digite um numéro: '))
res = sqrt(num)
print(f'A raiz de {num} é {ceil(res)}')
# importando a biblioteca random
import random
num = random.randint(1, 10)
print(num)