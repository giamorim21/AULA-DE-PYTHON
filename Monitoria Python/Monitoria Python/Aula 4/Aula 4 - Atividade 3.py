soma = 0
c = int(input("Digite a quantidade de notas você deseja receber: "))
for media in range(0, c):
    n = float(input("Digite o valor das notas: "))
    soma += n
m = soma / c
print(f"A média das notas é: {m:.2f}")