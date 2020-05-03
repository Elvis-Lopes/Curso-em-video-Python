def aumento (valor, aumento, format=True):
    total = 0
    if format:
        porcentagem = (valor*aumento)/ 100
        total = valor + porcentagem
        return moeda(total)
    else:
        return total


def reduzir (valor, reducao, format=True):
    total = 0
    if format:
        porcentagem = (valor * reducao) / 100
        total = valor - porcentagem
        return moeda(total)
    else:
        return total

def metade (valor, format=True):
    valor = valor/2
    if format:
         return moeda(valor)
    else:
        return valor

def dobro(valor, fomart=True):
    valor = valor * 2
    if fomart:
         return moeda(valor)
    else:
        return valor

def moeda(preco=0, moeda='R$' ):
    return f'{moeda}{preco:.2f}'.replace('.',',')

