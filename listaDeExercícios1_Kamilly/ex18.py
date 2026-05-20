print("=== Menu Interativo ===")
usuarios = ["Kamilly"]
print("Seja bem-vindo!")
opcao = 1
while opcao == 1 or opcao == 2:
    print("\nSelecione uma das opções abaixo:", "\n1 - Cadastrar usuário", "\n2 - Listar usuários", "\n3 - Sair")
    opcao = int(input("Digite a opção desejada (1/2/3): "))

    if opcao == 1:
        usuario = input("Digite o nome do novo usuário: ")
        usuarios.append(usuario)
    elif opcao == 2:
        print("\nUsuários listados:")
        for indice in range(0,len(usuarios)):
            print(usuarios[indice])
    elif opcao == 3:
        print("Menu fechando...")
        break
    else:
        print("Opção inválida. Digite somente entre 1, 2 ou 3.")