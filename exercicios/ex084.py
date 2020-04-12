dados = list()
pessoas = list()
opcao = str()
peso = list()

while True:
    opcao = str(input('Adicionar pessoa? [S/N]')).strip().upper()
    if 'S' in opcao:
        dados.append(str(input('Digite o nome: ')))
        dados.append(float(input('Digite o peso: ')))
        pessoas.append(dados[:])
        dados.clear()
    elif 'N' in opcao:
        break
    else:
        print('Opção inválida')
for p in pessoas:
    peso.append(p[1])

print(f'Foram cadastrados {len(pessoas)} pessoas\n'
      f'O menor peso é de {min(peso)}\n'
      f'O maior peso é de {max((peso))}')