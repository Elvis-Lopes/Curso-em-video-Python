def contador(i, f, p):
    """"
    Faz contagem e mostra na tela
    :i: inicio da contagem
    :f: final da contagem
    :p: retorna da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print()
    print('FIM!')
def somar(a, b, c=0):
    """"
    :param a: recebe o primeiro valor
    :param b: recebe o segundo valor
    :param c: recebe o terceiro valor (Opcional)
    :return: sem retorno
    """
    s = a + b + c
    return s
def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


help(contador)
help(somar)
resp = somar(1, 2)
n = int(input('Digite um numero: '))
print(f'O fatorial {n} é igual a {fatorial(n)}')

if par(n):
    print('Par')
else:
    print('Impar')


