def contador(inicio, fim, passo):
    from time import sleep

    for i in range(1, 11):
        print(f'{i} ', end='')
        sleep(1)
    print('Fim!')
    print('-='*30)

    for i in range(10, 0, -2):
        print(f'{i} ', end='')
        sleep(1)
    print('Fim')
    print('-='*30)

    if(inicio < fim):
        for i in range(inicio, fim, passo):
            print(f'{i} ', end='')
            sleep(1)
    elif(fim > inicio):
        passo *= -1
        for i in range(fim, inicio, passo):
            print(f'{i} ', end='')
            sleep(1)
    else:
        print('Paramêtros inválidos!')

    print('Fim')


contador(90,60 , 10)