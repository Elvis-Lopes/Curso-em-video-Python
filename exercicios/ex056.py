nome = str()
idade = 0
idadeMaisVelho = idade
nomeDoMaisVelho = str()
sexo = str()
contVinte = 0
totalIdade = 0
for i in range(0, 4):
    nome = str(input('Digite o nome: '))
    sexo = str(input('M/F')).upper().strip()
    idade = int(input('Digite a idade: '))
    totalIdade += idade
    if 'M' in sexo:
        if idade > idadeMaisVelho:
            nomeDoMaisVelho = nome
            idadeMaisVelho = idade
    if 'F' in sexo:
        if idade < 20:
            contVinte += 1
print(f'O homem mais velho se chama {nomeDoMaisVelho}\n'
      f'A {contVinte} mulheres com menos de 20 anos\n'
      f'A media de idade é {totalIdade/4}')
