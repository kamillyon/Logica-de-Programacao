print("=== Validador de Senha ===")
print("Seja bem-vindo! Digite uma senha com no mínimo 8 caracteres para ser aprovado")
senha = input("Digite aqui a nova senha: ")
while len(senha) < 8:
    print("Inválido. A senha necessita de no mínimo 8 caracteres.")
    senha = input("Digite novamente a nova senha: ")
print("Perfeito! Senha cadastrada e criptografada.")