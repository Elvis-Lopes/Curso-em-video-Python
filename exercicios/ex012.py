# Programa que mostre o preço do produto com 5% de desconto
preco = float(input('Insira o preoço do produto: '))
desc = (preco/100) * 5
novoPreco = preco - desc
print(f'o valor do produto é {preco:.2f}R$\n'
      f'com desconto aplicado é de {novoPreco:.2f}R$')