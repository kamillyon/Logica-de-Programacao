print("=== Ranking de Notas ===")
notas = []
for i in range (1,11):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    notas.append(nota)

notas.sort()
print("\nOrdem crescente:")
for i in range(0, len(notas)):
    print("Nota:", notas[i])

notas.sort(reverse=True)
print("\nOrdem decrescente:")
for i in range(0, len(notas)):
    print("Nota:", notas[i])