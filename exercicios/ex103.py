def fichaDoJogador (nome = '', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    return print(f'o jogador {nome} fez {gols} gol(s)')


nome = str(input('Digite o nome do jogador: ')).strip().title()
gol = str(input(f'Digite quantos gols o jogador fez: ')).strip()
fichaDoJogador(nome, gol)
