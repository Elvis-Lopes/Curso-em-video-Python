def linha(tam = 42):
    return '-' * tam


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


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[35m ')
    return opc