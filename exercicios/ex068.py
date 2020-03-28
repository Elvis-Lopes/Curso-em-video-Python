from random import randint
from time import sleep

jogador = maquina = cont = 0

while True:
    print('Jogador é par e o computador é impar')
    jogador = int(input('Digite um numero de 0 a 10: '))
    maquina = randint(0, 10)
    sleep(1)
    print('Impar ou par!!!')
    sleep(1)
    if (jogador+maquina) % 2 == 0:
        print(f'O computador jogou {maquina}')
        print('Jogador Venceu!')
        cont += 1
    else:
        print(f'O computador jogou {maquina}')
        print('Computador venceu!')
        break
print(f'O jogador teve {cont}  vitorias consecutivas')