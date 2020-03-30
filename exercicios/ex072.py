sequencia = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
             'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int()
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {sequencia[num]}')
        break
