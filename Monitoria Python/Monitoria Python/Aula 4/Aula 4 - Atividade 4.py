q = int(input("Digite a quantidade de números que deseja icluir na questão: "))

for change in range(0, q):
    num = int(input("Digite um número inteiro: "))
    if num <= 0:
        print("1")
    else:
        print(num)
