# exemplos da aula 17: Listas parte 1
# 1 exemplo:
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(4)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop()
print(num)
num.pop(2)
print(num)
num.remove(2)
print(num)
if 4 in num:
    num.remove(4)
    print(num)
else:
    print('Valor não encontrado')

# 2 exemplo
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

for ccont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
print(valores)

# exemplo 3
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}\n'
      f'Lista B: {b}')