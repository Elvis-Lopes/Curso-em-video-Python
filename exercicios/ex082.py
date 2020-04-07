numList = []
numPar = []
numImpar = []
opcao = int()

while True:
    opcao = int(input('1 - adicionar valor\n'
                      '2 - encerrar\n'))
    if opcao == 1:
        numList.append(float(input('Digite um valor: ')))
    else:
        break

for c in range(0, len(numList)):
    if numList[c] % 2.0 == 0:
        numPar.append(numList[c])
    else:
        numImpar.append((numList[c]))

print(f'Lista: {numList}\n'
      f'Lista de Pares: {numPar}\n'
      f'Lista de Impares: {numImpar}')