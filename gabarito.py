logado = False

while logado == False:
    
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a sua senha: ")

    if nome_usuario == "admin":
        if senha == "1234":
            logado = True
            print("\33[32mUsuário logado com sucesso!\033[m")
        else:
            for _ in range(2):
                senha = input("Senha incorreta! Tente novamente!")
                if senha == "1234":                  
                    print("Acesso concedido!")
                logado = True
                break
            else:
                print("Usuário Bloqueado, contate o T.I! ")
    else:
        print("Usuário não encontrado! ")

