numeros = [[], []]
valor = float()

for i in range(0, 7):
    valor = float(input('Digite um valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(f'Números par: {sorted(numeros[0])}\n'
      f'Numeros impar: {sorted(numeros[1])}')