import time
print("=== Gerador de Tabuada ===")

numero = int(input("Digite um número qualquer: "))
for i in range(1,11):
    multiplicacao = numero*i
    print(f"{i}multiplicado por {numero} = {multiplicacao}")
    time.sleep(1)