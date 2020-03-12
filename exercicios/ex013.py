# programa que efetua um reajuste de 15 % do salario de
# um funcioario

sal = float(input('Qual o salário do funcionario?\n'))
salReaj = sal + (sal * 15)/100
print(f'O salario do funcioanrio é {sal:.2f}R$ com o reajuste fica {salReaj:.2f}')