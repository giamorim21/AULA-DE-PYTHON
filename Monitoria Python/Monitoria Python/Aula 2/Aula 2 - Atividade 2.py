

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

if 0 < nota1 <= 10 and 0 < nota2 <= 10 and 0 < nota3 <= 10:
    media = (nota1 + nota2 + nota3)/3
    if media >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")
else:
    print("Nota inválida")