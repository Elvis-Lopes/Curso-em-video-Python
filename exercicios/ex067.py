n = 0
while True:
    n = int(input('Digite um numero: '))
    if n != 0:
        for c in range(0, 11):
            print(f'{n} x {c} = {n*c}')
    else:
        break