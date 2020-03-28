nomeDoMaisBarato = str()
opcao = soma = contMil = 0
nomeProduto = str(input('Insira o nome do produto: ')).strip()
valor = float(input('Valor do produto: '))
valorMaisBarato = valor
soma = soma + valor
while True:
    opcao = int(input('Deseja continua?\n'
                      '1- Sim\n'
                      '2- Não\n'))
    if opcao == 1:
        nomeProduto = str(input('Insirao o nome do  produto: ')).strip()
        valor = float(input('Insira o valor; '))
        soma = soma + valor
        if valor < valorMaisBarato:
            valorMaisBarato = valor
            nomeDoMaisBarato = nomeProduto
        if valor > 1000:
            contMil += 1
    if opcao == 2:
        break
print(f'Total da compra R${soma:.2f}\n'
      f'A {contMil} produtos acima de R$1000,00\n'
      f'O produto mais barato é {nomeDoMaisBarato}')
