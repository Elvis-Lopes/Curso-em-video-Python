contUm = contDez = contVinte = contCinquenta = 0
valor = int(input('Insira um valor: '))

while True:
    if valor >= 50:
        contCinquenta += 1
        valor -= 50
    elif valor >= 20:
        contVinte += 1
        valor -= 20
    elif valor >= 10:
        contDez += 1
        valor -= 10
    elif valor < 10 and valor > 0:
        contUm += 1
        valor -= 1
    else:
        break

print(f'{contCinquenta} notas de R$ 50\n'
      f'{contVinte} notas de R$ 20\n'
      f'{contDez} notas de R$ 10\n'
      f'{contUm} moedas de R$ 1 ')