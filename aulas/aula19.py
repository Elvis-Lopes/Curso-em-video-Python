pessoas = {'nome': 'Elvis',
           'sexo': 'M',
           'idade': 23}

print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Leandro'
print(pessoas)

pessoas['peso'] = 90
print(pessoas)

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
brasil.clear()

estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
