#Criar um lista que ter esses valores ( 5 , 1, 3 ,4 ,6 , 7 , 0)
lista =[5,1,3,4,6,7,0]
print(lista)

# faz como que eles virarem uma lista decrescente
lista.sort()
lista.reverse()
print(lista)

#Acrescente o valor 2 e 4  na lista
lista.extend([2,4])
print(lista)

#Depois mostra o tamanho da lista
print(len(lista))

#fala a posição do valor 5
print(lista[5])

#Apagar na lista a posição dois e colocar o valor 10
del lista[2]
print(lista)
lista.insert(2,10)
print(lista)

# Imprimir a lista
print(lista)