#algoritimo que mostre a tabuada do valor inserido
valor = int(input('Digite um valor: '))
print(f'tabuada do {valor}')
for i in range(0, 11):
    print(f'{valor} x {i} = {valor*i}')