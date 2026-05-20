print("=== Sistema de Média Escolar ===")
nota1, nota2, nota3 = 0, 0, 0
notas = [nota1, nota2, nota3]

for indice in range(0,3):
    vez = indice+1
    nota = float(input("Digite a nota" + str(vez) + "(0 a 10): "))
    while nota < 0 or nota > 10:
        print("Inválido.", "\nSomente nota de 0 a 10.")
        nota = float(input("Digite aqui a nota (0 a 10): "))
    notas[indice] = nota

soma = 0
for indice in range(0,3):
    soma += notas[indice]

media = soma/3
print(f"\nSua média foi: {media:.1f}")
if media >= 7: print("Aprovado!")
elif media >= 5 and media < 7: print("Recuperação.")
else: print("Reprovado.")