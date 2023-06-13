def calculadora(a,b):
    soma = a + b
    subtracao = a -b
    multiplicacao = a * b
    divisao = a / b

    return f"Soma: {soma}, Subtração: {subtracao}, Multiplicacao: {multiplicacao}, Divisao: {divisao}."

if __name__ == '__main__':
    a = int(input("Digite um valor para a: "))
    b = int(input("Digite um valor para b: "))
    print(calculadora(a,b))
