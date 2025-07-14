import random
import string

def gerar_senha(tamanho=6):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso
print("Senha gerada:", gerar_senha())       # Usa tamanho padrão 6
print("Senha com 12 caracteres:", gerar_senha(12))  # Usa tamanho personalizado