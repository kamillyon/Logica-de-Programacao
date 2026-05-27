print("=== Reajuste de Bolsa Auxílio ===")
valor = float(input("Digite o valor atual da bolsa auxílio do estagiário: "))
if valor < 1000:
    valor += (valor*0.15)
    print("Parabéns, você recebeu um aumento de 15%!",f"O novo valor da bolsa será de R${valor:.2f}")
else:
    valor += (valor*0.1)
    print("Parabéns, você recebeu um aumento de 10%!",f"O novo valor da bolsa será de R${valor:.2f}")