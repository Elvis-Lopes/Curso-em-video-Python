def notas(*num, sit=True):
    numeros = list()
    numeros =num[:]
    dicionarioDaSala = dict()

    if sit:
        dicionarioDaSala = {'Total: ': len(numeros),
                            'Maior:': max(numeros),
                            'Menor:': min(numeros),
                            'Media: ': sum(numeros)/len(numeros)}
    return dicionarioDaSala


res = notas(10, 5, 8)
print(res)