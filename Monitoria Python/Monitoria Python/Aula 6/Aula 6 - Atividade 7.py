num = 0
soma = 0
cont = 0
contPar = 0

while True:
    num = float(input("Digite um número: "))
    if num == -1:
        break
    soma += num
    cont += 1
    if num % 2 == 0:
        contPar += 1
media = soma / cont

porcentagem = contPar / cont * 100
print(f"A quantidade de elementos é: {cont}")
print(f"A soma dos números é: {soma}")
print(f"A média é igual: {media:.2f}")
print(f"A porcentagem de números pares é: {porcentagem:.2f}%")

