def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('o valor inserido não é númerico do tipo inteiro')
        except (KeyboardInterrupt):
            print('Usuario preferiu não digitar')
            break
        else:
            print(n)
            break
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('o valor inserido não é númerico do tipo real')
        except (KeyboardInterrupt):
            print('\nUsuario preferiu não digitar')
            break
        else:
            print(n)
            break



leiaInt('Digite um real inteiro: ')
leiaFloat('Digite um número real: ')