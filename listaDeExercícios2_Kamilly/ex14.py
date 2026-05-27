print("=== Carrinho de Compras Interativo ===")
itens = []
while True:
    item = input("Digite o nome do item de supermercado a ser adicionado: ").capitalize()
    itens.append(item)
    while True:
        opcao = input("\nDeseja adicionar mais itens ao carrinho? Digite 'continuar' para prosseguir ou 'sair' para finalizar: ").lower()
        if opcao != "continuar" and opcao != "sair":
            print("Opção inválida. Tente Novamente.")
            continue
        else:
            break
    if opcao == "continuar":
        continue
    else:
        break
print(f"\nOs itens no seu carrinho de compras são: {itens}")
