print("=== Desconto em e-books ===")
valor = float(input("Digite o valor do livo digital comprado: "))
if valor > 80:
    valor -= (valor*0.1)
    print("Você recebeu um desconto de 10%!", f"\nO valor final a ser pago é de R${valor:.2f}")
else:
    print(f"O valor a ser pago é de R${valor:.2f}")