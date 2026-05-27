print("=== Validador de Portas de Rede ===")
while True:
    porta = int(input("Digite uma porta de rede para liberar: "))
    if porta == 80 or porta == 443:
        print("Porta liberadda.")
        break
    else:
        print("Porta bloqueada, tente outra.")
