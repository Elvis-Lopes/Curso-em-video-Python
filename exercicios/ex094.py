pessoas = dict()
listaDePessoas = list()
listaDeMulheres = list()
opcao = str()
mediaIdade = float()

pessoas['nome'] = str(input('Digite o nome: ')).strip().title()
pessoas['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().title().upper()[0]
pessoas['idade'] = int(input('Digite a idade: '))
listaDePessoas.append(pessoas.values())
if 'F' in pessoas['sexo']:
    listaDeMulheres.append(pessoas.values())

while True:
    opcao = str(input('Deseja continuar ? [S/N]'))[0].title().strip().upper()
    if 'N' in opcao:
        break
    else:
        pessoas['nome'] = str(input('Digite o nome: ')).strip().title()
        pessoas['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().title().upper()[0]
        pessoas['idade'] = int(input('Digite a idade: '))
        listaDePessoas.append(pessoas.values())
        if 'F' in pessoas['sexo']:
            listaDeMulheres.append(pessoas.values())

print(listaDeMulheres)
print(f'O grupo tem {len(listaDePessoas)} pessoas')
print('As mulheres cadastradas foram: ', end='')
for c in range(0, len(listaDeMulheres)):
    print(f'{listaDeMulheres[c]["nome"]} ', end='')
