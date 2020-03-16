# program que leia um número de 0 a 9999 mostre na tela cada um dos digitos separados
num = int(input('Digite um numero: '))
n = num // 1 % 10
print(f'analisando o numero {num}')
print(f'Unidade: {n}')
n = num // 10 % 10
print(f'Dezena: {n}')
n = num // 100 % 10
print(f'Centena: {n}')
n = num // 1000 % 10
print(f'Milhar: {n}')
