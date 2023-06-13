nota = 0
maior = 0
count = 0
while True:
    if nota == -1:
        break
    nota = float(input("Digite uma nota: "))
    if nota >= maior:
        count += 1
        maior = nota

print(f"A maior nota: {maior}")
print(f"Quantidade de notas: {count}")