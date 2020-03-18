# exemplos de estruturas condicionais
# Exemplo 1: condição simples
nome = str(input('Qual é o seu nome? '))
if nome == 'Elvis':
    print('Que nome lindo você tem, ', end='')
print('bom dia!')

# Exemplo 2: condição composta
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1 + n2)/2
if m > 6:
    print(f'Sua média foi {m:.1f} você foi aprovado!')
else:
    print(f'Sua média foi {m:.1f} você foi reprovado!')
