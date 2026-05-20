print("=== Reserva de Assentos ===")
assentos = [
    ["[L]","[L]","[L]"],
    ["[L]","[L]","[L]"],
    ["[L]","[L]","[L]"]
]
fileiras = ["A ","B ","C "]

print("Formação de Assentos da sala 01")
print("   1 "," 2 "," 3 ")
for posicao, linha in enumerate(assentos):
    print(f"{fileiras[posicao]}" + " ".join(linha))
coluna = int(input("Qual a coluna que você deseja selecionar (1, 2 ou 3): "))
while coluna != 1 and coluna != 2 and coluna != 3:
    print("Opção inválida. Digite apenas um número entre 1 e 3.")
    coluna = int(input("Qual a coluna que você deseja selecionar (1, 2 ou 3): "))
fileira = (input("Qual a fileira que você deseja selecionar (A, B, C): ")).upper()
while fileira != "A" and fileira != "B" and fileira != "C":
    print("Opção inválida. Digite apenas um número entre A, B ou C.")
    fileira = (input("Qual a fileira que você deseja selecionar (A, B, C): ")).upper()

if coluna == 1:
    coluna = 0
elif coluna == 2:
    coluna = 1
else:
    coluna = 2

if fileira == "A":
    fileira = 0
elif fileira == "B":
    fileira = 1
else:
    fileira = 2

assentos[fileira][coluna] = "[X]"

print("\n   1 "," 2 "," 3 ")
for posicao, linha in enumerate(assentos):
    print(f"{fileiras[posicao]}" + " ".join(linha))
print("Assento escolhido ocupado.")
