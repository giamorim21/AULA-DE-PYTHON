def multiplo(a):
    if a % 2 == 0:
        return "O número é múltiplo de 2."
    else:
        return "O número não é múltiplo de 2."

if __name__ == '__main__':
    a = int(input("Digite um número: "))
    print(multiplo(a))
