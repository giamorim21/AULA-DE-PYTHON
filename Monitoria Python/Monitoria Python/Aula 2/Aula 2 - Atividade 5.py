x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))
a = input("Escolha entre as seguintes opções: Soma, Subtracao, Multiplicacao, Divisao: ")

if a == 'Soma':
    print(x + y)
elif a == 'Subtracao':
    print(x - y)
elif a == 'Multiplicacao':
    print(x*y)
elif a == 'Divisao':
    print(x/y)