teste = list()
teste.append('Elvis')
teste.append(23)
print(teste)

galera = list()
galera = [['joão', 19], ['Ana', 13], ['Joaquim', 33]]
galera.append(teste[:])

print(galera)
print(galera[1][0])

dado = list()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
