print("=== Urna Eletrônica ===")
candidatas = ["Marie Curie", "Ada Lovelace", "Rosalind Franklin", "Katherine Johnson"]
candidata1, candidata2, candidata3, candidata4 = 0,0,0,0

while True:
    i = 1
    for candidata in candidatas:
        print(f"{i} - {candidata}")
        i += 1
    print("0 - Sair")
    voto = int(input("Digite o número da candidata que deseja como líder do squad (Ou 0 para sair): "))
    if voto <0 or voto>4:
        print("\nOpção inválida. Tente novamente")
        continue
    elif voto == 0:
        break
    
    if voto == 1:
        candidata1 += 1
    elif voto == 2:
        candidata2 += 1
    elif voto == 3:
        candidata3 += 1
    else:
        candidata4 += 1

print("Votação Encerrada.", f"\n{candidatas[0]} recebeu {candidata1} voto(s).", f"\n{candidatas[1]} recebeu {candidata2} voto(s)", f"\n{candidatas[2]} recebeu {candidata3} voto(s)", f"\n{candidatas[3]} recebeu {candidata4} voto(s)")
