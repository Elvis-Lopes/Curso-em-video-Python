def mostrarLinha():
    print('-='*30)
def mensagem(msg):
    print('-='*30)
    print(msg)
    print('-='*30)
def soma(n1, n2):
    s = n1 + n2
    print(s)
def contador(*num):
    print(num)
def dobrarValor(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1
    print(lst)


mostrarLinha()
print('Teste')
mostrarLinha()
mensagem('Olá mundo')
mostrarLinha()
soma(5, 7)
soma(7.8, 9.54)
contador(5, 4, 3)
contador(9, 10, 8, 7, 5)
dobrarValor([4, 3, 2, 1])
