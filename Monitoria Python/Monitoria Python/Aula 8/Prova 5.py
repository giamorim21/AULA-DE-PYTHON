lista = [1, 5, 8, 10, 12]
print(f"Lista original: {lista}")
# A) Acrescente o valor 3 e 4  na lista
lista.extend([3,4])
# B) Faça com que eles virem uma lista decrescente
lista.sort()
lista.reverse()
# C) Depois mostre o tamanho da lista
print(f"O tamanho da lista é: {len(lista)}")
# D) Apaga a primeira posição da lista e coloca o valor 35
del lista[0]
lista.insert(0,35)
# E) Imprimir a lista
print(lista)