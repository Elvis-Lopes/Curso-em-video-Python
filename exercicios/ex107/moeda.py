def aumento (valor, aumento):
    porcentagem = (valor*aumento)/ 100
    total = valor + porcentagem
    return moeda(total)


def reduzir (valor, reducao):
    porcentagem = (valor * reducao) / 100
    total = valor - porcentagem
    return moeda(total)


def metade (valor):
    valor = valor/2
    return moeda(valor)

def dobro(valor):
    valor = valor * 2
    return moeda(valor)

def moeda(preco=0, moeda='R$' ):
    return f'{moeda}{preco:.2f}'.replace('.',',')