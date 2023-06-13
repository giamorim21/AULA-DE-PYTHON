"""fat = int(input("Qual é o número que você quer calcular? "))
result = 1
for x in range(fat, 0, -1):
    result *= x

print(result)"""

# segunda forma com função
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(0))
