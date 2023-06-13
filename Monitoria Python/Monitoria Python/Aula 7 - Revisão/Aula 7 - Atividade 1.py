# Primeira forma de fazer o exercicio

"""def ler_dados():
    dados = []
    while True:
        entrada = input("Digite o CNPJ e a quantidade de funcionários (ou digite 'sair' para finalizar): ")
        if entrada.lower() == "sair":
            break
        CNPJ, qtd_funcionarios = map(int, entrada.split(","))
        dados.append((CNPJ, qtd_funcionarios))
    return dados


def encontrar_maior_empresa(dados):
    maior_empresa = 0
    maior_qtd_fucionarios = 0
    for CNPJ, qtd_fucionarios in dados:
        if qtd_fucionarios > maior_qtd_fucionarios:
            maior_empresa = CNPJ
            maior_qtd_fucionarios = qtd_fucionarios
    return maior_empresa, maior_qtd_fucionarios


if __name__ == '__main__':
    dados = ler_da7 dos()
    maior_empresa, maior_qtd_funcionarios = encontrar_maior_empresa(dados)
    print(f"Maior empresa: {maior_empresa}, quantidade {maior_qtd_funcionarios}")"""

#dados = []
#CNPJ = 0
#qtd_func = 0
#maior = 0
#maior_qtd_func = 0

# Segunda forma de fazer o exercício

#while True:
#   entrada = input("Digite o CNPJ e a quantidade de funcionários\ne caso queira sair do loop digite 'sair': ")
#    if entrada.lower() == 'sair':
#       break
#    CNPJ, qtd_func = map(int, entrada.split(","))  # map utilizado para transformar
#    dados.append((CNPJ, qtd_func))                 # os valores em números inteiros
#for CNPJ, qtd_func in dados:
#    if qtd_func > maior_qtd_func:
#        maior = CNPJ
#        maior_qtd_func = qtd_func
#print(f"Maior empresa é: {maior} e quantidade: {maior_qtd_func}")

# Terceira fomra de fazer o exercício
valores = list(map(str , input("Digite o CNPJ e o número de funcionarios: ").split(' ')))
impares = []
print(valores)

for x in range(len(valores)):
    if (x%2!=0):
        impares.append(valores[x])
        maior = max(impares)

pos_cnpj_maior = valores.index(maior)-1
print(f"CNPJ:{valores[pos_cnpj_maior]}, número de funcionarios: {maior}")

