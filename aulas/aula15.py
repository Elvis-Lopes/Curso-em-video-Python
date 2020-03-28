# exemplos de while
# 1:
cont = 1
while cont <= 10:
    print(cont, '=>', end='')
    cont += 1
print('Acabou')
# 2:
cont = 1
while True:
    print(cont, '=>', end='')
    cont += 1
# 3:
n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))

# 4:
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')