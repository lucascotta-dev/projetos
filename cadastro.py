usuarios = {}

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Cadastrar Usuário")
    print("2 - Fazer login")
    print("3 - Esqueci minha senha")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("\n=== Cadastro de Usuário ===")
        nome = input("Digite o seu nome: ")
        email = input("Digite o seu email: ")
        if email in usuarios:
            print("Este email já está cadastrado. ")
        else:
            senha = input("Digite a sua senha: ")
            usuarios[email] = {"nome": nome,"senha": senha}
            print(f"Usuário: {nome} cadastrado com sucesso!")
    elif opcao == "2":
        print("\n=== Login ===")
        email = input("Digite o seu email: ")
        senha = input("Digite sua senha: ")
        if email not in usuarios:
            print("Usuário não encontrado! ")
        else:
            if usuarios[email]["senha"] == senha:
                print(f"Bem-vindo, {usuarios[email]['nome']}!")
                break
            else:
                print("Senha incorreta.")
    elif opcao == "3":
        print("\n=== Recuperar Senha ===")
        email = input("Digite seu email cadastrado: ")
        if email not in usuarios:
            print("Usuário não encontrado!")
        else:
            nova_senha = input("Digite uma nova senha: ")
            usuarios[email]["senha"] = nova_senha
            print("Senha atualizada com sucesso!")
    elif opcao == "4":
        print("Encerrando o sistema! Obrigado!")
        break
    else:
        print("Opção inválida! Tente novamente! ")

