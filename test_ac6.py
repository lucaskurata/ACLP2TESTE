def menor(lista, i, f):
    m = lista[i]
    for j in range(i+1, f+1):
        if lista[j] < m:
            m = lista[j]
    return m

def test_menor_1():
    lista = [30,10,20,40,50]
    assert menor(lista, 0, len(lista)-1) == 10

def test_menor_2():
    lista = [30,10,20,40,50]
    assert menor(lista, 3, 4) == 40

def test_menor_3(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,50]
    menor(lista, 0, 5) == 20

def test_menor_4(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,'A']
    menor(lista, 0, 4) == 20

def test_menor_5(): # Faça um except para esse tipo de erro
    lista = [30,10,20,40,5]
    menor(lista, 4, 1) == 5

