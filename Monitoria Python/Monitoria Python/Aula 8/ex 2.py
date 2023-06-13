contPar = 0
contImpar = 0
contPositivo = 0
contNegativo = 0

for x in range (5):
    c = int(input("Digite um número: "))
    if c % 2 == 0:
        contPar += 1
    if c % 2 != 0:
        contImpar += 1
    if c > 0:
        contPositivo += 1
    if c < 0:
        contNegativo += 1

print(f"{contPar} valor(es) par(es)\n"
      f"{contImpar} valor(es) impar(es)\n"
      f"{contPositivo} valor(es) positivo(s)\n"
      f"{contNegativo} valor(es) negativo(s)"
      )
