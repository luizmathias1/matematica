def ex2():
    def pg(razao,valorInicial):
        valorInicial = valorInicial*razao
        return valorInicial






    razao = float(input("Digite o valor da razão"))
    valorInicial = float(input("Digite o valor inicial"))
    vezes = int(input("digite a quantidade de valores que você"
                          "deseja printar"))

    for i in range(vezes):
        print(pg(razao, valorInicial))
        valorInicial = valorInicial*razao

"""Exercicio 8-----------"""

def a8():
    razao = 3
    vi = 1
    for i in range(10):
        print(vi)
        vi = razao * vi
def b8():
    razao = 1/2
    vi = 2
    for i in range(10):
        print(vi)
        vi = razao * vi

def c8():
    print("pode ter mais de um valor possível")

def d8():
    print("pode ter mais de um valor possível")

def ex9(n): #n é o n-ésimo número que deseja obter
    if n == 1:
        return 1
    else:
        return ex9(n-1) + n
print(ex9(11))

def ex10(n):
    razao = 3
    vi = 50000
    for i in range(n):
        vi = razao * vi
    print(vi)
print(ex10(4)) #4 é a quantidade de tempo(pode ser qualquer valor)
"""Entre 1h e 2h a população excederá 200000 bactérias"""


def rotina(L, j):
    if j == 1:
        return L
    i = L.index(max(L[:j]))
    L[i], L[j - 1] = L[j - 1], L[i]
    return rotina(L, j - 1)


L = [3, 7, 4, 2, 6]
resultado = rotina(L, len(L))
print(resultado)

def ex3(numero):
    if numero == 2:
        return True
    elif numero < 2:
        return False
    elif ex3(numero - 3) or (numero % 2 == 0 and ex3(numero // 2)):
        return True
    else:
        return False

numeros = [6, 7, 19, 12]

for numero in numeros:
    if ex3(numero):
        print(f"{numero} pertence a T")
    else:
        print(f"{numero} NÃO pertence a T")

def cadeias_impares_de_zeros(n, prefix=""):
    if n == 0:
        print(prefix)
    else:
        # Adiciona "0" à cadeia existente.
        cadeias_impares_de_zeros(n - 1, prefix + "0")
        # Adiciona "1" à cadeia existente.
        cadeias_impares_de_zeros(n, prefix + "1")

n = 7  # Número de zeros desejados (número ímpar).
cadeias_impares_de_zeros(n)





            




