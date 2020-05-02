c = ('\033[n,',
     '\033[0;30;41m')

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  msg')
    print('~'*tam)
    print(c[0], end='')

comando = str()
while True:
    titulo('SISTEMA DE JUDA PYHELP', 1)
    comando = str(input('Função ou biblioteca >')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)