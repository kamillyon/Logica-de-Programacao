print("=== Sistema de Boletim ===")
alunos = []
notas = []
resultado = []

for i in range(0,5):
    nome = input(f"Digite o nome do aluno {i+1}: ").capitalize()
    alunos.append(nome)
    nota = float(input(f"Digite a média final de {nome}: "))
    notas.append(nota)
    if nota >= 7:
        resultado.append("Aprovado")
    else:
        resultado.append("Reprovado")

print("\nResultados finais:")
for i in range(0,5):
    print(f"Aluno: {alunos[i]}"
          f"\nMédia final: {notas[i]}"
          f"\nResultado: {resultado[i]}"
          "\n")
