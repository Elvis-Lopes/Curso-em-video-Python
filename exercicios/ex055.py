peso = float(input('Digite o peso'))
maiorPeso = peso
menorPeso = peso

for i in range(0, 5):
    peso = float(input('Digite o peso: '))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
        
print(f'Maior peso: {maiorPeso:.2f}Kg\n'
      f'Menor peso: {menorPeso:.2f}Kg')
