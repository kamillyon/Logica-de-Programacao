print("=== Controle de Estoque ===")
produto = input("Digite o nome do produto: ")
quant_atual = int(input("Digite a quantidade atual de " + produto + ": "))
quant_vendida = int(input("Digite a quantidade vendida de " + produto + ": "))
estoque = quant_atual - quant_vendida

print("\nEstoque restante:", estoque)
if estoque < 0:
    print("ALERTA!", "O estoque está negativo. Sua quantidade atual está menor do que a quantidade vendida, é necessário comprar novos produtos urgentemente.")
elif estoque <= 10:
    print("Seu estoque possui pouco produto.", "É necessário comprar mais para suprir as vendas!")
else:
    print("Seu estoque ainda possui produto suficiente!")

continuar = int(input("Gostaria de verificar o estoque de outro produto? (0 = Sim; 1 = Não): "))
while continuar == 0:
    produto = input("Digite o nome do produto: ")
    quant_atual = int(input("Digite a quantidade atual de " + produto + ": "))
    quant_vendida = int(input("Digite a quantidade vendida de " + produto + ": "))
    estoque = quant_atual - quant_vendida

    print("\nEstoque restante:", estoque)
    if estoque < 0:
        print("ALERTA!", "O estoque está negativo. Sua quantidade atual está menor do que a quantidade vendida, é necessário comprar novos produtos urgentemente.")
    elif estoque <= 10:
        print("Seu estoque possui pouco produto.", "É necessário comprar mais para suprir as vendas!")
    else:
        print("Seu estoque ainda possui produto suficiente!")
    continuar = int(input("Gostaria de verificar o estoque de outro produto? (0 = Sim; 1 = Não): "))

