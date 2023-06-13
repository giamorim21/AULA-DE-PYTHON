salario = float(input("Digite um valor: "))

if salario <= 0:
    print("O salário está inválido!")
elif salario < 1200:
    print("O salário está fora da legislação!")
else:
    print("O salário está dentro da legislação!")

