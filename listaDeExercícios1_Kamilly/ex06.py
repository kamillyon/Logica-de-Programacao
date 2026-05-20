print("=== Classificador de Notas ===")
nota = float(input("Digite aqui a nota (0 a 10): "))
while nota < 0 or nota > 10:
    print("Inválido.", "\nSomente nota de 0 a 10.")
    nota = float(input("Digite aqui a nota (0 a 10): "))
if nota >= 7: print("Aprovado!")
elif nota >= 5 and nota < 7: print("Recuperação.")
else: print("Reprovado.")