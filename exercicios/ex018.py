# programa que lé um ângulo qualquer e devolve o seno, cosseno e tangente
# de um triangulo
import math

angulo = float(input('Insira o angulo do traingulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f'Seno: {seno}\n'
      f'cosseno: {cosseno}\n'
      f'tangente: {tangente}')