hora = float(input("Digite qual é a hora agora: "))

if 0 <= hora < 6:
    print("Boa madrugada!")
elif 6 <= hora < 12:
    print("Bom dia!")
elif 12 <= hora < 18:
    print("Boa tarde!")
elif 18 <= hora <= 24:
    print("Boa noite!")