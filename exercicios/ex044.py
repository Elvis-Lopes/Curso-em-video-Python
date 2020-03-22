formaDePagamento = int(input('Qual a forma de pagamento?\n'
                             '1 - A vista no dinheiro ou cheque\n'
                             '2 - A vista no cartão\n'
                             '3 - Parcelado em 2 vezes\n'
                             '4 - Parcelado em 3 vezes\n'))
valor = float(input('valor da compra: '))
valorTax = float()
if formaDePagamento == 1:
    valorTax = (valor * 10)/100
    valor = valor - valorTax
    print(f'Total: R${valor:.2f}')
elif formaDePagamento == 2:
    valorTax = (valor * 5)/100
    valor = valor - valorTax
    print(f'Total: R${valor:.2f}')
elif formaDePagamento == 3:
    valor = valor / 2
    print(f'Valor das parcelas R${valor:.2f}')
else:
    valorTax = (valor * 20)/100
    valor = (valor + valorTax) / 3
    print(f'Valor das parcelas R%{valor:.2f}')