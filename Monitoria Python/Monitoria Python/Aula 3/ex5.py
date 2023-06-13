def operador(a,b):

    return a + b, a - b, a * b, a / b

if __name__ == '__main__':
    a = int(input("Digite um valor para a: "))
    b = int(input("Digite um valor para b: "))
    print(operador(a,b))
