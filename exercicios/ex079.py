listaNum = []
opcao = int()
valor = float()

while True:
    opcao = int(input('1- Adicionar valor\n'
                      '2- Encerrar\n'))
    if opcao == 1:
        valor = float(input('Digite o valor: '))
        if valor not in listaNum:
            listaNum.append(valor)
    else:
        break
print(f'Os valores da lista são: {listaNum}')