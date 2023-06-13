nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

if 0 < nota1 <= 10 and 0 < nota2 <= 10 and 0 < nota3 <= 10:
    media = (nota1*1 + nota2*1.5 + nota3*2)/4.5
    if media >= 9:
        print("Aluno tirou SS")
    elif 7 < media < 9:
        print("Aluno tirou MS")
    elif 5 < media < 7:
        print("Aluno tirou MM")
    elif 2 < media < 5:
        print("Aluno tirou MI")
    elif 0 < media < 2:
        print("Aluno tirou II")
    elif media == 0:
        print("Aluno tirou SR")
else:
    print("Nota inválida")