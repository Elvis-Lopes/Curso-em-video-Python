boletim = []
aluno = []
opcao = str()

while True:
    opcao = str(input('Adicionar aluno? [S/n]')).strip().upper()
    if 'S' in opcao:
        aluno.append(str(input('Digite o nome do aluno: ')))
        aluno.append(int(input('Nota 1: ')))
        aluno.append(int(input('Nota 2: ')))
        boletim.append(aluno[:])
        aluno.clear()
    elif 'N' in opcao:
        break
    else:
        print('Opção inválida')

for p in boletim:
    print(f'Aluno: {p[0]}\n'
          f'Nota 1: {p[1]}\n'
          f'Nota 2: {p[2]}\n'
          f'Media: {(p[1]+p[2]/2)}\n')
    print('-='*30)

