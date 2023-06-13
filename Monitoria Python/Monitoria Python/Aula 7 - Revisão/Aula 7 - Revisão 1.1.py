dados = []
CNPJ = 0
qtd_func = 0
maior = 0
maior_qtd_func = 0
count = 0

valorSaida = float(input("Entre com o valor de saída: "))

while CNPJ != valorSaida and qtd_func != valorSaida:
    entrada = input("Digite o CNPJ e a quantidade de funcionários: ")

    if CNPJ == valorSaida and qtd_func == valorSaida:
        print("Nenhum dado foi fornecido.")
        break

    count += 1
    CNPJ, qtd_func = map(int, entrada.split(","))  # map utilizado para transformar
    dados.append((CNPJ, qtd_func))                 # os valores em números inteiros
for CNPJ, qtd_func in dados:
    if qtd_func > maior_qtd_func:
        maior = CNPJ
        maior_qtd_func = qtd_func
print(f"Maior empresa é: {maior} e quantidade: {maior_qtd_func}")

