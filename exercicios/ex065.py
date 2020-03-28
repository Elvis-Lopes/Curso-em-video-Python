media = soma = 0
cont = 1
n = int(input('Digite um número: '))
menor = menor = n
opcao = str()
while opcao != 'N':
    opcao = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if opcao in 'S':
        n = int(input('Digite um numero: '))
        if n < menor:
            menor = n
        if n > maior:
            maior = n
        soma = soma + n
        cont += 1
print(f'Você digitou {cont} numeros e a média foi {soma/cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
