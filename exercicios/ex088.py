from random import randint
megaSena = []
jogo = []
quantidadeDeJogos = int(input('Quantos jogos  deseja: '))
rodada = 1

for c in range(0, quantidadeDeJogos):
    for i in range(0, 6):
        jogo.append(randint(1, 60))
    megaSena.append(jogo[:])
    jogo.clear()

for p in megaSena:
    print(f'jogo {rodada}: {p}')
    rodada += 1