nomeCompleto = str(input('Insira o seu nome completo: ')).strip().title()
nome = nomeCompleto.split()
print(f'Primeiro nome é {nome[0]}')
print(f'Ultimo nome é {nome[len(nome)-1]}')
