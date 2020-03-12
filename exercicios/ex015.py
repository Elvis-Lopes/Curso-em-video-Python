# programa que calcula o valor do aluguel de um carro
dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos Km rodados?  '))
valorFinal = dias * 60 + 0.15 * km
print(f'O valor do aluguel é de {valorFinal:.2f}R$')
