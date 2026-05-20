print("=== Sistema de login ===")
usuario = "admin"
senha = "1234"

usuario1 = input("Usuário: ")
senha1 = input("Senha: ")

if usuario1 != usuario or senha1 != senha: print("Credenciais inválidas.", "\nUsuário ou senha incorretos.")
else: print("Login realizado com sucesso!")