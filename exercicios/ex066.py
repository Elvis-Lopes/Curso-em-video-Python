n = soma = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n != 999:
        soma = soma + n
        cont += 1
    else:
        break
print(f'A soma dos {cont} valores foi {soma}')
