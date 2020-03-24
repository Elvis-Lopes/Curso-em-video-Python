idadePessoas = int()
menorDeIdade = 0
maiorDeIdade = 0
for i in range(0, 7):
    idadePessoas = int(input('Digite a idade'))
    if idadePessoas >= 18:
        maiorDeIdade += 1
    else:
        menorDeIdade += 1
print(f'{maiorDeIdade} são maiores de idade e {menorDeIdade} são menor de idade')
