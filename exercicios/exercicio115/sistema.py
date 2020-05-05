from exercicios.exercicio115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do Sistema.. Ate logo')
    else:
        print('Erro!')
    sleep(0.5)