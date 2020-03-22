r1 = float(input('Insira a reta: '))
r2 = float(input('Insira a reta: '))
r3 = float(input('Insira a reta: '))

if r1 < r2 + r3:
    print('é possível formar um triangulo')
elif r2 < r1 + r3:
    print('é possível formar um triangulo')
elif r3 < r2 + r3:
    print('é possível formar um triangulo')
else:
    print('não é possível formar um triangulo')