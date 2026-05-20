print("=== Sistema de Autenticação com Tentativas ===")
usuario = "admin"
senha = 1234
tentivas = 1
tentativa_usuario = input("Digite o usuário: ")
tentativa_senha = int(input("Digite a senha (Apenas números): "))
if tentativa_usuario != usuario and tentativa_senha != senha:
    print("Usuário ou senha incorretos")
    while tentativa_usuario != usuario and tentativa_senha != senha:
        tentivas += 1
        print("\nTente novamente")
        tentativa_usuario = input("Digite o usuário: ")
        tentativa_senha = int(input("Digite a senha (Apenas números): "))
        if tentativa_usuario != usuario and tentativa_senha != senha:
            print("Usuário ou senha incorretos")
        if tentivas == 3:
            print("\nConta Bloqueada.")
            break
else: print("\nConta acessada!")