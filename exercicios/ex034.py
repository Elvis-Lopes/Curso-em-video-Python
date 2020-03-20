sal = float(input('Insira o salário: '))
aumento = float()
if sal > 1250:
    aumento = (sal*15)/100
    sal = sal + aumento
else:
    aumento = (sal*10)/100
    sal = sal + aumento
print(f'Novo salario R${sal:.2f}')
