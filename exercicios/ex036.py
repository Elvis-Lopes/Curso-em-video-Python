sal = float(input('informa o seu salario: '))
anos = int(input('Em quantos anos irá pagar?'))
meses = anos * 12
mensalidade = sal / meses
taxa = (sal * 30)/100
if mensalidade > taxa:
    print('Recusado')
else:
    print('Aprovado')
