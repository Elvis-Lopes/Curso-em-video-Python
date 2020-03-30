times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo'
         'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Game',
         'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense',
         'Avaí')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os quatro ultimos são: {times[19:14:-1]}')
print(f'Em ordem alfabetica: {sorted(times)}')
for pos, time in enumerate(times):
    if 'Chapecoense' in times[pos]:
        print(f'O Chapecoense esta na posição {pos}')
