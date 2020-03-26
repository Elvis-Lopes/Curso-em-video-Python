primeiroTermo = float(input('Insira o primeiro termo: '))
razao = float(input('Insira a razão: '))
i = 0
while i < 10:
    print(f'{primeiroTermo}, ', end='')
    primeiroTermo = primeiroTermo + razao
    i += 1