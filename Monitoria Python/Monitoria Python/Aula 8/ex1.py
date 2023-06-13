while True:
    nome = str(input("Digite o nome do atleta\n(ou deixe em branco para parar o loop): "))

    if nome == "":
        break

    saltos = []

    for i in range(1,6):
        distancia = float(input("Digite a distância alcançsada no salto {1}: "))
        saltos.append(distancia)

    media = sum(saltos) / len(saltos)
    print(f"A média é de {media}")
