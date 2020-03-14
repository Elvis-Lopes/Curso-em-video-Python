# semelhante ao 19 só que sorteando a ordem de apresentação dos alunos
import random
aluno = []

for i in range(0, 4):
    aluno.append(input('Insira o nome do aluno: '))

random.shuffle(aluno)
print(f'a ordem de apresentação é {aluno}')
