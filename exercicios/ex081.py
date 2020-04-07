numList = []
opcao = int()
while True:
    opcao = int(input('1 - Inserir valor\n'
                      '2 - Encerrar\n'))
    if opcao == 1:
        numList.append(float(input('Digite um valor: ')))
    else:
        break
print(f'na lista {numList}:\n'
      f'Foram digitados {len(numList)} valores\n'
      f'A lista em ordem decrescente é {sorted(numList, reverse=True)}\n')
if 5 in numList:
    print('O número 5 esta lista')
else:
    print('O número 5 não esta lista')