print("=== Dashboard Simples ===")
vendas = [
    [120, 300, 250],
    [400, 150, 600]
    ]

total_geral = 0
maior_venda = 0

i = 1
print("=== Vendas da semana ===")
for linha in vendas:
    print(f"Venda da semana {i}: {linha}")
    i +=1

i = 1
print()
for linha in vendas:
    total_linha = 0
    total_linha = sum(linha)
    total_geral += total_linha
    for valor in linha:
        if valor > maior_venda:
            maior_venda = valor
    print(f"Total da linha {i}: {total_linha}")
    i += 1
print(f"Total Geral: {total_geral}", f"\nMaior venda: {maior_venda}")
