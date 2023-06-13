#Criar um lista que ter esses valores ( 20 , 40 ,30 ,10 , 0 )
lista = [0,20,10,40,30]

#faz como que eles virarem uma lista decrescente
lista.sort()
lista.reverse()
print(lista)

#Apaga a posição dois(2) e mostrar o valor apagado
v = lista.pop(2)
print(f"O número removido é: {v}")

#Inserir o valor dois (2) na posição quatro (4)
lista.insert(4, 2)
print(lista)

#tamanho da lista0
print(len(lista))

