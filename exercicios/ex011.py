# programa que le a largura e altura de uma parede calcula sua are
# e informa quantos litros de tinta será necessario para pintar
# cada litro pinta 2m quadrados

altura = float(input('Insira a altura da parede: '))
largura = float(input('Insira a largura da parede:'))
area = altura * largura
print(f'A área e de {area} metros quadrados')
litroTinta = area / 2
print(f'será necessário {litroTinta} litros de tinta para pintar a parede')
