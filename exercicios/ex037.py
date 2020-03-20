import math
num = int(input('Insira um número: '))
conv = int(input('1- Binario\n2- Octal\n3- Hexadecimal'))
if conv == 1:
    print(f'Conversão em binario: {bin(num)}')
elif conv == 2:
    print(f'Conversão para Octal: {hex(num)}')
elif conv == 3:
    print(f'Conversão para hexadecimal: {hex(num)}')
else:
    print('Opção invalida')
