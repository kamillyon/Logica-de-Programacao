print("=== Caixa de Supermercado ===")
precos = []
subtotal = 0
for i in range(1,6):
    preco = float(input("Digite aqui o preço do produto " + str(i) + " (configuração do preço: XXX.XX): "))
    precos.append(preco)
for indice in range(0,5):
    subtotal += precos[indice]
imposto = subtotal*0.1
total = subtotal+imposto
print(f"\nSubtotal: R${subtotal:.2f}", f"\nImposto: R${imposto:.2f}", f"\nValor final: R${total:.2f}")
