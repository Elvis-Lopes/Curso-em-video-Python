r1 = float(input('Insira a reta: '))
r2 = float(input('Insira a reta: '))
r3 = float(input('Insira a reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('é possível formar um triangulo', end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('isósceles')
else:
    print('não é possível formar um triangulo')

