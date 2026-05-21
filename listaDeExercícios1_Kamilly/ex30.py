print("=== Sistema de Gerenciamento ===")
menu = ["Cadastrar produtos", "Listar produtos", "Buscar produto", "Remover produto", "Salvar em arquivo", "Ler arquivo", "Sair"]
produtos = []
def exibir_menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        i = 0
        for funcao in menu:
            print(f"{i} - {funcao}")
            i += 1
        opcao = int(input("Digite uma opção: "))
        if opcao == 0: 
            cadastrar_produtos(produtos)
        elif opcao == 1: 
            listar_produtos(produtos)
        elif opcao == 2: 
            buscar_produto(produtos)
        elif opcao == 3: 
            remover_produto(produtos)
        elif opcao == 4: 
            salvar_arquivo()
        elif opcao == 5: 
            ler_arquivo()
        elif opcao == 6: 
            sair()
            break
        else:
            print("Opção inválida. Tente novamente")

def cadastrar_produtos(produtos):
    produto = input("Digite o nome do produto: ").capitalize()
    produtos.append(produto)
    print("Produto adicionado!")
    
def listar_produtos(produtos):
    print("\n=== PRODUTOS ARMAZENADOS ===")
    for produto in produtos:
        print(f"- {produto}")

def buscar_produto(produtos):
    produto = input("Digite o produto que você deseja buscar: ").capitalize()
    if produto in produtos:
        print(f"{produto} está em produtos armazenados")
    else:
        print(f"{produto} não está em produtos armazenados")

def remover_produto(produtos):
    print("\n=== Produtos Armazenados ===")
    if len(produtos) == 0:
        print("Não há produtos para remover.")
        return
    while True:
        i = 0
        for produto in produtos:
            print(f"{i} - {produto}")
            opcao = int(input("Digite o número correspondente ao produto que você deseja remover: "))
        if opcao >= 0 and opcao < len(produtos): 
            produtos.pop(opcao)
            print("Produto removido.")
            break
        else:
            print("Opção inválida. Tente novamente")

def salvar_arquivo():
    nome_arq = input("Digite no qual o arquivo deve ser salvo: ")
    conteudo = input("O que você deseja que tenha escrito dentro do arquivo: ")
    with open(nome_arq,"w", encoding="utf-8") as arq:
        arq.write(conteudo)
    print("Arquivo criado!")

def ler_arquivo():
    nome_arq = input("Digite no qual o arquivo deve ser salvo: ")
    try:
        with open(f"{nome_arq}","r", encoding="utf-8") as arq:
            print("\n--- Conteúdo do Arquivo ---")
            print(arq.read())
    except FileNotFoundError:
        print("Ops! Parece que esse arquivo não existe...")

def sair():
    print("Fechando sistema...")
    print("Até mais!")

exibir_menu()
