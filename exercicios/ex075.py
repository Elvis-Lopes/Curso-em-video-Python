num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))
num3 = float(input('Digite um numero: '))
num4 = float(input('Digite um numero: '))
contPar = 0
tuplaNumeros = (num1, num2, num3, num4)

for i in range(0, len(tuplaNumeros)):
    if tuplaNumeros[i] % 2 == 0:
        contPar += 1

print(f'Você digitou os valores {tuplaNumeros}\n'
      f'O valor 9 apareceu {tuplaNumeros.count(9)} vezes\n'
      f'Os valores pares digitados foram {contPar}')