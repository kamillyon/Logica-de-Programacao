print("=== Conversor de Moedas ===")
valor_reais = float(input("Digite um valor em Reais (R$): R$"))
cotacao_dolar = float(input("Digite o valor da cotação atual do Dólar (US$): US$"))
valor_dolares = valor_reais/cotacao_dolar
print(f"O valor de R${valor_reais:.2f} é equivalente a US${valor_dolares:.2f}")