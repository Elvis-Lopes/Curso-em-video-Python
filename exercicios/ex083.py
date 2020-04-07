abreParentenses = 0
fechaParenteses = 0
expressao = input('Digite a expressão matematica: ')
for c in expressao:
    if '(' in c:
        abreParentenses += 1
    if ')' in c:
        fechaParenteses += 1
if abreParentenses == fechaParenteses:
    print('Expressão valida')
else:
    print('Expressão inválida')
