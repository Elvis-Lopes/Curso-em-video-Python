# crie um programa que recebe o nome completo de uma pessoa e exibe
# Nome com todas as letras maiusculas
nome = input('Insira o seu nome completo ').strip()

# Nome com todas as letras maiusculas
print(nome.upper())

# Nome comm todas as letras minusculas
print((nome.lower()))

# Quantas letras tem o nome sem consideras os espaços
print(len(nome)-nome.count(' '))

# Quantas letras tem o primeiro nome
primeiroNome = nome.split()
print(len(primeiroNome[0]))