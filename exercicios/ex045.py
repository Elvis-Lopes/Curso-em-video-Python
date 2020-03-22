from random import randint
while True:
    usuario = int(input('1- Pedra\n'
                        '2- Papel\n'
                        '3- Tesoura\n'))
    computador = randint(1, 3)
    if usuario == 1 and computador == 3:
        print('Pedra vence de tesoura')
        break
    elif usuario == 1 and computador == 2:
        print('Pedra perde para papel')
    elif usuario == 2 and computador == 1:
        print('Papel vence de pedra')
        break
    elif usuario == 2 and computador == 3:
        print('Papel perde para tesoura')
    elif usuario == 3 and computador == 1:
        print('Tesoura perde para pedra')
    elif usuario == 3 and computador == 2:
        print('Tesoura vence de papel')
        break
    else:
        print('Empate')
print('Parabens você venceu')