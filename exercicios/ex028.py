from random import randint
while True:
    num = int(input('Digite um numero de 0 a 5'))
    maquina = randint(0, 5)
    if num == maquina:
        print('Acertou!')
        break
    else:
        print('Errou')
