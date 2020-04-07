listaNum = []
for c in range(0, 5):
    listaNum.append(int(input('Digite um valor: ')))
print(f'O maior valor da lista é {max(listaNum)} que esta no posição {listaNum.index(max(listaNum))}\n'
      f'O menor valor da lista é {min(listaNum)} que esta na posicação {listaNum.index(min(listaNum))}')