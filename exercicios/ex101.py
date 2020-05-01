from datetime import datetime
def voto(nascimento):
    anoAtual = datetime.now()
    idade = anoAtual.year - nascimento
    if idade < 16:
        return print(f'com a {idade} não pode votar')
    elif idade > 16 and idade < 18 or idade >60:
        return print(f'com a idade {idade} o voto é opcional')
    else:
        return print(f'com a idade {idade} o voto é obrigatorio')


idade = int(input('Digite o ano do seu nascimento: '))
resposta = voto(idade)
