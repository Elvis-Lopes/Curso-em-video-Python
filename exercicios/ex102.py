from math import factorial
def fatorial (num=1, show=True):
    if show:
        return factorial(num)
    else:
        fatorial(num)
        return 'Fatorial calculado'

r = fatorial(5, False)
print(r)