def maior(*num):
    listaNumeros = num[:]
    maiorValor = num[0]
    for i in range(1, len(listaNumeros)):
        if listaNumeros[i] > maiorValor:
            maiorValor = listaNumeros[i]
    print(f'O maior valor é {maiorValor}')


maior(1, 2, 2, 5, 3, 8, 9, 0)