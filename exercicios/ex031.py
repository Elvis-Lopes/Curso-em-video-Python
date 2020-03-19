distancia = float(input('Distancia da viagem: '))
preco = float()
if distancia < 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da viagem é de R${preco:.2f}')