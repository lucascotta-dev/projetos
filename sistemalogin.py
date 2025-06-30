# Faça um sistema que peça o nome de usuário e senha de uma pessoa
# Se o nome for "admin" e a senha for "1234", iremos exibir a mensagem "Seja bem vindo Patrão"
# Caso contrário exiba a mensagem de "Acesso negado"

#Faça com que esse sistema rode em looping enquanto exiba a mensagem de "usuário não encontrado" 
# se o nome não for admin, E também de "senha incorreta" caso a senha não seja "1234"


while True:
    
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a sua senha: ")

   

    if nome_usuario == "admin" and senha == "1234":
        print("Seja bem vindo Patrão")
        break
    else:
        if nome_usuario != "admin":
            print("Usuário não encontrado")
        if senha != "1234":
            print("Senha incorreta")


