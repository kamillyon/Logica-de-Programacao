print("=== Relatório de Vendas ===")
opcao = 0
vendas = []
while opcao == 0:
    venda = float(input("Digite o valor da sua venda (Configuração XXX.XX): "))
    vendas.append(venda)
    opcao = int(input("Gostaria de adicionar mais um valor? (0=Sim; 1=Não): "))

maior_venda = max(vendas)
menor_venda = min(vendas)
total_vendido = sum(vendas)
media = total_vendido / len(vendas)
print(f"\nO total vendido foi R${total_vendido:.2f}, sendo a menor venda R${menor_venda:.2f} e a maior R${maior_venda:.2f}",f"\nA média foi R${media:.2f}")
    