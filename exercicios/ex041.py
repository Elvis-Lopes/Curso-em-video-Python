from datetime import date

nascimento = int(input('Insira o ano de nascimento: '))
dataAtual = date.today()
idade = dataAtual.year - nascimento

if idade < 9:
    print('Mirim')
elif idade >= 9 and idade < 14:
    print('Infantil')
elif idade >= 14 and idade <= 19:
    print('Junior')
elif idade == 20:
    print('Senior')
else:
    print('Master')
