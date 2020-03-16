# cria um programa que receba o nome de uma cidade e informe se começa ou não com a palavra SANTO
cidade = str(input('Insira o nome da cidade: ')).strip()
cidade = cidade.split()
if 'SANTO' in cidade[0].upper():
    print('a cidade começa com nome SANTO')
else:
    print('a cidade não começa com nome SANTO')
