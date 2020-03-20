# exemplos de estrutura condicional aninhada
nome = str(input('Qual é o seu nome: ')).strip().title()
if nome == 'Elvis':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'João' or nome =='Maria':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')
