# exemplos de Tuplas
# 1
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
# mostrando um dos itens da tupla
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
# usando for para exibir a tupla
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(sorted(lanche))
# 2
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
