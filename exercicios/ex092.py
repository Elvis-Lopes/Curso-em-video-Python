from datetime import datetime

anoAtual = datetime.now()
pessoa = dict()

pessoa['nome'] = str(input('Digite o nome: ')).strip().title()
pessoa['nascimento'] = int(input('Digite o ano de nascimento: '))
pessoa['ctps'] = int(input('Insira o CTPS (digite 0 caso não tiver): '))
pessoa['idade'] = anoAtual.year - pessoa['nascimento']

if pessoa['ctps'] == 0:
    print('-='*30)

    print(f'Nome: {pessoa["nome"]}\n'
          f'Idade: {pessoa["idade"]}\n'
          f'CTPS: não tem')
else:
    pessoa['anoDeContratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Digite o salario: '))
    aposentadoria = pessoa['anoDeContratacao'] + 35
    aposentadoria = aposentadoria - anoAtual.year
    pessoa['idadeDeAposentar'] = pessoa['idade'] + aposentadoria

    print('-='*30)

    print(f'Nome: {pessoa["nome"]}\n'
          f'Idade: {pessoa["idade"]}\n'
          f'CTPS: {pessoa["idade"]}\n'
          f'Ano de contratação: {pessoa["anoDeContratacao"]}\n'
          f'Salário: {pessoa["salario"]}\n'
          f'idade para se aposentar: {pessoa["idadeDeAposentar"]}')
