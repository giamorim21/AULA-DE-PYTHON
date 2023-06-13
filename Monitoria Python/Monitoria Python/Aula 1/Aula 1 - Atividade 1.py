#Atividade 1
#Receba (input) uma base e uma altura e calcule/mostre a área de um triângulo
# area = (base * altura) / 2
# a) não usando input
# b) usando input

# a) Sem input
base = 10
altura = 5

area = (base * altura) / 2
print(f"Essa é a área do triângulo: {area}")

# b) Com input
base = input("Digite um valor para a base: ")
altura = input("Digite um valor para a altura: ")

area = (float(base) * float(altura)/2)
print(f"Essa é a área do triângulo: {area}")