dadosDoJogador = dict()
golsFeitos = list()

dadosDoJogador['nome'] = str(input('Digite o nome: ')).strip().title()
dadosDoJogador['partidas'] = int(input(f'Quntas partidadas {dadosDoJogador["nome"]} participou? '))

for c in range(0, dadosDoJogador['partidas']):
    golsFeitos.append(int(input(f'Quantos gols {dadosDoJogador["nome"]} fez na partida {c+1}? ')))

dadosDoJogador['gols'] = golsFeitos
dadosDoJogador['total'] = sum(golsFeitos)
print('-='*30)
print(dadosDoJogador)

print('-='*30)
print(f'Nome do jogador: {dadosDoJogador["nome"]}\n'
      f'Quantidade de partidas: {dadosDoJogador["partidas"]}\n'
      f'Gols feitos nas partidas: {dadosDoJogador["gols"]}\n'
      f'Total de gols: {dadosDoJogador["total"]}')

print('-='*30)
print(f'O jogador {dadosDoJogador["nome"]} jogou {dadosDoJogador["partidas"]} partidas.')
for c in range(0, dadosDoJogador['partidas']):
    print(f'    => Na partida {c+1}, fez {dadosDoJogador["gols"][c]}')
print(f'Foi um total de {dadosDoJogador["total"]} gols')