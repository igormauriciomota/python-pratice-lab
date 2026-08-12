"""
 Exercício 1 - Login básico

Objetivo: entender cadastro simples e comparação de credenciais.

"""

print("--- CADASTRO ---")
# Recebe os dados do usuario
login_cadastro = input("Crie seu login: ").strip().lower()
senha_cadastro = input("Crie sua senha: ").strip()

print("\n--- LOGIN ---")

login = input("Login: ").strip().lower()
senha = input("Senha: ").strip()

# As duas condiçoes precisam ser verdadeiras.
if login == login_cadastro and senha == senha_cadastro:
    print("Login realizado com sucesso.")
else:
    print("Login ou senha invalidos.")


