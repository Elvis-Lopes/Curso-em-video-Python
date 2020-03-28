idade = maiorIdade = qtdHomens = qtdMulheres =0
sexo = str()
opcao = str
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Qual o sexo da pessoa? F/M')).strip().upper()[0]
    if sexo in 'M':
        qtdHomens += 1
    if sexo in 'F':
        if idade < 20:
            qtdMulheres += 1
    if idade >= 18:
        maiorIdade += 1
    opcao = str(input('Deseja continua? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
print(f'A {maiorIdade} maiores de idade\n'
      f'Foram cadastrados {qtdHomens} homens\n'
      f'Ha {qtdMulheres} mulheres com menos de 20 anos')