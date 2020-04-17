situacaoAluno = {}

situacaoAluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().title()
situacaoAluno['Media'] = float(input(f'Digite a média do {situacaoAluno["Nome"]}: '))

if situacaoAluno['Media'] >= 7:
    situacaoAluno['Resultado'] = 'Aprovado'
else:
    situacaoAluno['Resultado'] = 'Reprovado'

print(f'Nome do aluno: {situacaoAluno["Nome"]}\n'
      f'Media do aluno: {situacaoAluno["Media"]:.2f}\n'
      f'Situação do aluno: {situacaoAluno["Resultado"]}')
