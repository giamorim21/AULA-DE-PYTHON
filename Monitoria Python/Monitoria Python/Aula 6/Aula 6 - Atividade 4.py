soma = 0
count = 0
while True:
    nota = int(input("Digite uma nota: "))
    if nota == -1:
        break
    soma += nota
    count += 1
media = soma / count
print(f"A media é igual {media}")