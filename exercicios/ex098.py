def contador(inicio, fim, passo):
    from time import sleep

    print('Iniciando contagem de 1 a 10')
    for i in range(0, 11):
        print(f'{i}, ', end='', flush=False)
        sleep(0.5)
    print()

    print('Iniciando contagem regressiva de 2 em 2')
    for i in range(10, -1, -2):
        print(f'{i}, ', end='', flush='')
        sleep(0.5)
    print()

    print('Iniciando contagem personalizada')
    if inicio < fim and passo != 0:
        while inicio <= fim:
            print(f'{inicio}, ', end='', flush=False)
            sleep(0.5)
            inicio += passo
    elif inicio > fim and passo != 0:
        while inicio >= fim:
            print(f'{inicio}, ', end='', flush=False)
            sleep(0.5)
            inicio -= passo
    elif inicio < fim and passo == 0:
        while inicio <= fim:
            print(f'{inicio}, ', end='', flush=False)
            sleep(0.5)
            inicio += 1
    else:
        while inicio >= fim:
            print(f'{inicio}, ', end='', flush=False)
            sleep(0.5)
            inicio -= 1

contador(95, 90, 0)