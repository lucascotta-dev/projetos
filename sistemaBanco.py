conta = {}

conta['numeroConta'] = input("Digite o número da sua conta: ")
conta['nomeCompletoPessoa'] = input("Digite o seu nome completo: ")
conta['cpf'] = input("Digite o seu CPF: ")
conta['saldo'] = float(input("Digite o seu saldo: "))

while True:
    print("\n=== MENU BANCO ===")
    print("1 - Consultar saldo: ")
    print("2 - Sacar: ")
    print("3 - Depositar: ")
    print("4 - Sair: ")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {conta['saldo']:.2f}")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if valor <= conta['saldo']:
            conta['saldo'] -= valor
            print(f"Saque realizado com sucesso! Novo saldo: R$ {conta['saldo']:.2f}")
        else:
            print("Saldo insuficiente!")
    
    elif opcao == "3":
        valor = float(input("Digite o valor do depósito: "))
        conta['saldo'] += valor
        print(f"Depósito realizado com sucesso! Novo saldo: R$ {conta['saldo']:.2f}")
    
    elif opcao == "4":
        print("Você está saindo do sistema! Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Opção inválida. Tente novamente.")
        