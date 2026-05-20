import random
print("=== Verificador de Números Pares ===")
numeros = []
pares = 0
print("Números sorteados:")
for i in range(0,10):
    numero = random.randint(1,100)
    numeros.append(numero)
    print(numero)
for indice in range(0, len(numeros)):
    if numeros[indice] % 2 == 0:
        pares += 1
print("Dos números sorteados", pares, "são pares.")