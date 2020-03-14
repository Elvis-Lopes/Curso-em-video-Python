# programa que recebe o nome de 4 alunos e sortea que vai apagar o quadro
import random
aluno = []

for i in range(0, 4):
    aluno.append(input('Insira o nome do aluno: '))

sorteio = random.randint(0, 3)
print(f'O aluno que vai apagar o quadro é {aluno[sorteio]}')