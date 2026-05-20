print("=== Lista de Tickets ===")
continuar = 0
chamados = ["Impressora não está funcionando", "Erro 404 ao tentar emitir relatório", "Tela de carregamento infinita no site do SENAI", "Baixar Packet Tracer", "Atualizar servidor", "Mudar as senhas dos administradores"]
while continuar == 0:
    print("\nChamados abertos: ")
    posicao = 0
    for chamado in chamados:
        print(posicao, "-", chamado)
        posicao += 1
    opcao = int(input("\nQual chamada você concluiu: "))
    while opcao <0 or opcao > (posicao-1):
        print("Opção inválida. Digite um número de 0 a", (posicao-1))
        opcao = int(input("\nQual chamada você deseja modificar: "))
    posicao = 0

    chamados.pop(opcao)
    print("\nPerfeito! Chamado removido da lista dos pendentes.", "Lista atualizada:")
    for chamado in chamados:
        print(posicao, "-", chamado)
        posicao += 1
    
    continuar = int(input("Deseja concluir mais algum chamado? (Sim = 0; Não = 1): "))
    while continuar != 0 and continuar != 1:
        print("Opção Inválida. Digite 0 para 'Sim' e 1 para 'Não'")
        continuar = int(input("Deseja concluir mais algum chamado? (Sim = 0; Não = 1): "))