listaDeProdutos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
                     'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('Lista de Produtos')
for i in range(0, len(listaDeProdutos), 2):
    print(f"{listaDeProdutos[i]:.<30} R$ {listaDeProdutos[i+1]:.2f}")
    