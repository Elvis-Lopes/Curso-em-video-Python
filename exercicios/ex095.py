jogador = dict()
listaDeJogadores = list()
golsFeitos = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['partidas'] = int(input('Quantas partidas jogou? '))
    for c in range(0, jogador['partidas']):
        golsFeitos.append(int(input(f'Quantos gols foram feitos na partida {c+1}: ')))
    jogador['gols'] = golsFeitos[:]
    listaDeJogadores.append(jogador.copy())
    jogador.clear()
    golsFeitos.clear()

    opcao = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if 'N' in opcao:
        break
