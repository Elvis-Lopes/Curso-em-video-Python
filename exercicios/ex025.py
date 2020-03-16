# recebe um programa que recebe o nome completa e informa se tem silva como sobrenome
nome = input('Insira o nome completo: ').strip().title()
if 'SILVA' in nome.upper():
    print(f'o nome {nome} tem Silva')
else:
    print(f'o nome {nome} não tem Silva')
