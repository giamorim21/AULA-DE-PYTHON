count = 0
countPar = 0
soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == -1:
        break
    soma += num
    count += 1
    if num % 2 == 0:
        countPar += 1

media = soma / count
porcentagem = countPar / count * 100

print(f"Quantidade de elementos dados é: {count}")
print(f"Soma dos valores é: {soma}")
print(f"A média dos valores é: {media}")
print(f"A porcentagem de números pares é: {porcentagem:.2f}%")
