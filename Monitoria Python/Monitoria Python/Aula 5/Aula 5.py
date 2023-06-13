import statistics

ident = [1,2,3]
print(ident)

lista = ['Joao', 'Maria', 'Carlos', 'Eduardo', 'Cristiane']
print(lista)
lista[2]
print(lista[2])
print(len(lista))
lista.insert(3,'Giovana')
print(lista)
lista.remove('Giovana')
print(lista)

del lista[0]
print(lista)

lista.append('Kaynan')
print(lista)

print(lista.index('Carlos'))
if 'Giovana' in lista:
    print("Valor está na lista")
else:
    print("Valor não está na lista")

print(lista.count('Maria'))
lista [0] = 'Giovana'
print(lista)

lista1 = [1,5,3,4,2]
novaLista = sorted(lista1)
print(sorted(lista1))
print(lista1)

print(max(lista1))
print(min(lista1))
print(sum(lista1))

lista2 = [10,10,10,10]
media = statistics.mean(lista2)
print(media)

