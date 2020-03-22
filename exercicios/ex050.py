soma = 0
for c in range(0, 6):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        soma = soma + n
print(f'Resultado: {soma}')