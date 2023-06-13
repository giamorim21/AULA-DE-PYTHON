numeros = []

while True:
    num = int(input("Digite um número: "))
    if num == -1:
        break
    numeros.append(num)
print(numeros)
print(f"O maior número é {min(numeros)}")
print(f"O menor número é {max(numeros)}")

maior = 0
menor = 0
while True:
    x = int(input("digite um número: "))
    if x == -1:
        break
    if x > maior:
        maior = x
    if x < menor:
        menor = x
print(f"Maior: {maior} Menor: {menor}")