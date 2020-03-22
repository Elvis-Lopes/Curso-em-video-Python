from datetime import date

anoAtual = date.today()
anoNascimento = int(input('Insira o seu ano de nascimento: '))
idade = anoAtual.year - anoNascimento

if idade < 18:
    print(f'Falta {18 - idade} anos para se alistar')
elif idade == 18:
    print(f'Esta na hora de se alistar ')
else:
    print(f'Já passou {idade - 18} para você se alistar')
