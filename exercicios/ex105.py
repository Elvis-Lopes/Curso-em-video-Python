def notas(*num, sit=True):
    numeros = list()
    numeros =num[:]
    dicionarioDaSala = dict()
    media = sum(numeros)/len(numeros)
    desempenho = str()
    dicionarioDaSala = {'Total: ': len(numeros),
                        'Maior:': max(numeros),
                        'Menor:': min(numeros),
                        'Media: ': media}
    if sit:
        if media >7:
            desempenho = 'Excelente'
            dicionarioDaSala = {'Total: ': len(numeros),
                                'Maior:': max(numeros),
                                'Menor:': min(numeros),
                                'Media: ': media,
                                'Situação': desempenho}
        elif media <= 6.9 and media > 5:
            desempenho = 'Bom'
            dicionarioDaSala = {'Total: ': len(numeros),
                                'Maior:': max(numeros),
                                'Menor:': min(numeros),
                                'Media: ': media,
                                'Situaçao: ': desempenho}
        elif media <= 4.9:
            desempenho = 'Horrivel'
            dicionarioDaSala = {'Total: ': len(numeros),
                                'Maior:': max(numeros),
                                'Menor:': min(numeros),
                                'Media: ': media,
                                'Situaçao: ': desempenho}
        else:
            desempenho = ''
            dicionarioDaSala = {'Total: ': len(numeros),
                                'Maior:': max(numeros),
                                'Menor:': min(numeros),
                                'Media: ': media,
                                'Situaçao': desempenho}
    else:
        dicionarioDaSala = {'Total: ': len(numeros),
                            'Maior:': max(numeros),
                            'Menor:': min(numeros),
                            'Media: ': media}
    return dicionarioDaSala


res = notas(4, 8, 8, sit=False)
print(res)