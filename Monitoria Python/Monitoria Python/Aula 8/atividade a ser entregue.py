# a) Usando for



# b) Usando função

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
       termo = fibonacci(n-1)
       termo.append(termo[-1] + termo[-2])
       return termo

n = int(input('Quantos termos? '))
seq = fibonacci(n)
print(f"Sequência de fibonacci: {seq}")
