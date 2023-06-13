num = 0.0
count = 0
soma = 0
while num != -1:
    num = float(input("Digite um valor: "))
    if num != -1:
        soma += num
        count += 1
media = soma / count
print(f"A média é igual {media}")
