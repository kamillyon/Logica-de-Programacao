print("=== Classe de IP ===")
while True:
    primeiro_octeto = int(input("Digite o primeiro octeto de um endereço IP: "))
    if primeiro_octeto >= 1 and primeiro_octeto <= 126:
        print(f"O primeiro octeto {primeiro_octeto} é da classe A.")
        break
    elif primeiro_octeto >= 128 and primeiro_octeto <= 191:
        print(f"O primeiro octeto {primeiro_octeto} é da classe B.")
        break
    elif primeiro_octeto >= 192 and primeiro_octeto <= 223:
        print(f"O primeiro octeto {primeiro_octeto} é da classe C.")
        break
    else:
        print("Primeiro octeto inválido. Tente novamente")
        continue