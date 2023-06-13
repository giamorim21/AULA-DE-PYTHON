# a) Faça uma tabuada usando FOR dentro de um while

while True:
    numero = int(input("Digite um número (1 a 10) para ver sua tabuada (ou 0 para saiar): "))

    if numero == 0:
        print("Encerrar o programa...")
        break

    if numero < 1 or numero > 10:
        print("Número invalido. Digite novamente.")
        continue

    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# b) Faça um código, usando FOR , que mostre todas as tabuadas (1 até 10)


