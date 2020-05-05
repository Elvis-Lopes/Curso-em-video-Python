from exercicios.ex111.utilidadesCeV.dados import leiaDinheiro

def aumento (valor=0.0, aumento=0.0, format=True):
    leiaDinheiro(valor)
    total = 0
    if format:
        porcentagem = (valor*aumento)/ 100
        total = valor + porcentagem
        return moeda(total)
    else:
        return total


def reduzir (valor=0.0, reducao=0.0, format=True):
    total = 0
    if format:
        porcentagem = (valor * reducao) / 100
        total = valor - porcentagem
        return moeda(total)
    else:
        return total

def metade (valor=0.0, format=True):
    valor = valor/2
    if format:
         return moeda(valor)
    else:
        return valor

def dobro(valor=0.0, fomart=True):
    valor = valor * 2
    if fomart:
         return moeda(valor)
    else:
        return valor

def moeda(preco=0.0, moeda='R$' ):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(valor = 0.0, aumen=0.0, reducao=0.0, format=True):
    print('-='*30)
    print('Resumo do valor'.center(30))
    print('-='*30)
    print(f'Preço Analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{aumen}% de aumento: \t{aumento(valor, aumen)}')
    print(f'{reducao}% de redução: \t{reduzir(valor, reducao)}')