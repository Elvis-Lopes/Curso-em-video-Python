pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if opcao in 'N':
        break
    if opcao not in 'SN':
        print('ERRO! digite S ou N')
        opcao = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
        if 'N' in opcao:
            break
print('-='*30)
print(f'ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é {media:.2f}')
print('As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'pessoas com idade acima da media: ', end='')
for p in galera:
    if p['idade'] > media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<= Encerrado =>')