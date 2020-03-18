frase = str(input('Insira uma frase: ')).strip().upper()
# abaixo ira contar quantas vezes aparece a letra A
vezesA = frase.count('A')

# abaixo mostra em qual posição apareceu a primeira letra A
primeiroA = frase.find('A')

# abaixa mostra em qual posição apareceu a ultima letra A
ultimaA = frase.rfind('A')

print(f'a letra "A" aparece {vezesA} vezes, o primeira "A" esta no posição {primeiroA} e o ultimo na {ultimaA}')