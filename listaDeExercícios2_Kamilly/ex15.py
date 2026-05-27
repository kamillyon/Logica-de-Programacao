print("=== Contador de Vogais ===")
frase = input("Digite uma frase qualquer: ").lower()
letras = list(frase)
vogais = 0

for letra in letras:
    if letra in 'aàáâãeêéiíoôóõuú':
        vogais += 1

print(f"A frase '{frase.capitalize()}' contém {vogais} vogais.")
