n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

while True:

    opcao = int(input('[1] - somar\n'
          '[2] - multiplicar\n'
          '[3] - maior\n'
          '[4] - Novos numeros\n'
          '[5] - Sair do programa\n'))

    if opcao == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior é o {n1}')
        elif n1 < n2:
            print(f'O maior é {n2}')
        else:
            print('Os numeros são iguais')
    elif opcao == 4:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite um numero'))
    elif opcao == 5:
        print('Saindo...')
        break
    else:
        print('Opção invalida')