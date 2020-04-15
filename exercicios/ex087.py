matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaDosPares = 0
somaDaTerceiraColulna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            somaDosPares = somaDosPares+matriz[l][c]
        if matriz[l][2]:
            somaDaTerceiraColulna = somaDaTerceiraColulna + matriz[l][2]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é: {somaDosPares}\n'
      f'A soma dos valores da terceira coluna é {somaDaTerceiraColulna}\n'
      f'O maior valor da segunda linha é {max(matriz[1])}')
