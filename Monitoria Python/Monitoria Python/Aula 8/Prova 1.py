while True:
    senha = int(input("Digite o valor que você acha que é a senha: "))
    if senha == 2002:
        print("Acesso Permitido!")
        break
    else:
        print("Senha Inválida. Tente novamente!")
