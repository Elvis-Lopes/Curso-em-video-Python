num1 = float(input('Insira um numero: '))
num2 = float(input('Insira um numero: '))
num3 = float(input('Insira um numero: '))
if num1 > num2 and num1 > num3:
    print(f'O maior numéro é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior numero é {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior numero é {num3}')
else:
    print('numero iguais')

