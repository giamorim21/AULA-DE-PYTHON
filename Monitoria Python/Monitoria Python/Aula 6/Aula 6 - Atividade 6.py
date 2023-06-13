maior = 0
nota = 0
soma = 0
cont = 0
aprovado = 0
reprovado = 0
quantidade = 0

valorSaida = float(input("Entre com o valor de saída: "))

while nota != valorSaida:
    nota = float(input("Digite a nota do aluno: "))

    if nota == valorSaida:
        break
    soma += nota
    quantidade += 1

    if nota > maior:
        cont = 1
        maior = nota
    elif nota == maior:
        cont += 1
    if nota < 5:
        reprovado += 1
    else:
        aprovado += 1
print("Alunos Aprovados:", aprovado)
print("\nAlunos Reprovados: ",reprovado)
print("\nMaior nota: {:.2f}\nQuantidade de nota: {}\n".format( maior, cont))
if quantidade > 0:
    print("Media da turma: ",soma)