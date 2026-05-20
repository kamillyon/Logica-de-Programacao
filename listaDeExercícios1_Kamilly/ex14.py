print("=== Cadastro Múltiplo de Usuários ===")
usuarios = []
for i in range(1,6):
    usuario = input("Digite o nome do usuário " + str(i) + ": ")
    usuarios.append(usuario)

print(usuarios)