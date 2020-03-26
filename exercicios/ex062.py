while True:
    opcao = int(input('1- Nova PA \n2- Sair do programa\n'))
    if opcao == 1:
        primeiroTermo = float(input('Insira o primeiro termo: '))
        razao = float(input('Insira a razão: '))
        for i in range(0, 10):
            print(f'{primeiroTermo}, ', end='')
            primeiroTermo = primeiroTermo + razao
    elif opcao == 2:
        print('Saindo...')
        break
    else:
        print('Opção invalida')
    print('\n')
