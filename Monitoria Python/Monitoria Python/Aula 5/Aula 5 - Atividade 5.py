import statistics

lista = []
for a in range(0, 5):
    num = int(input("Digite um número:"))
    lista.append(num)
media = statistics.mean(lista)
print(media)