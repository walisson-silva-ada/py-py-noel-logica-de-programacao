lista = [0, 1, -2, 3, 7, -4, 9, -6, -8]
print(lista)

def maior_recursivo(lista, item = 0):
    ultimo_item = len(lista) - 1
    if item == ultimo_item:
        return lista[item]
    maior = lista[item]
    comparar = maior_recursivo(lista, item + 1)
    if maior > comparar:
        return maior
    else:
        return comparar

print(maior_recursivo(lista))
