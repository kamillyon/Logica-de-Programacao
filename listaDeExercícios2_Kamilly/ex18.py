print("=== Detector de Palíndromo")
palavra = input("Digite uma palavra aleatória: ").lower()
letras = list(palavra)
letras_invertidas = palavra[::-1]
if "".join(letras) == letras_invertidas:
    print("Sua palavra é um palíndromo!")
else:
    print(f"Hum...sinto muito. {palavra} não é um palíndromo, ao contrário fica {letras_invertidas}")
