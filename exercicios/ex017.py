# programa que calculra o cateto oposto, adjacente e hipotnusa
import math
catetoOposto = float(input('Insira o cateto oposto: '))
catetoAdjacente = float(input('Insira o cateto adjacente: '))
hipotenusa = math.hypot(catetoAdjacente, catetoOposto)
print(f'Hipotenusa: {hipotenusa:.2f}')