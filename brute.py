import time

def descobridor_senha_4_digitos(senha_real):
    tentativas = 0
    
    print("BREAK THAT SHIT!!!")
    
    for tentativa in range(10000):  # 0000 até 9999
        senha_tentativa = f"{tentativa:04d}"  # garante 4 dígitos com zeros à esquerda
        tentativas += 1

        print(f"Tentando senha: {senha_tentativa}")

        if senha_tentativa == senha_real:
            print(f"Senha encontrada: {senha_tentativa} em {tentativas} tentativas!")
            return senha_tentativa
        
        time.sleep(0.001)  # delay entre as tentativas

    print("Senha não encontrada.")
    return None

# Como usar:
senha = "7657"
descobridor_senha_4_digitos(senha)
