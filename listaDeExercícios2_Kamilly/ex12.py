print("=== Fatorial Simples ===")
fatorial = 1
while True:
    numero = int(input("Digite um número inteiro positivo qualquer: "))
    if numero > 0:
        break
    else:
        print("O número deve ser INTEIRO e POSITIVO. Tente novamente, por favor.")
        continue
for i in range(1, numero+1):
    fatorial *= i
print(f"O fatorial de {numero} é igual a {fatorial}")