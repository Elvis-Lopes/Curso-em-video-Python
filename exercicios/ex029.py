velocidade = int(input('Insira a velocidade: '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print(f'Multa de R${multa:.2f}')
else:
    print('Não foi multado')