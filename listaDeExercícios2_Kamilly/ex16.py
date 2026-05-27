import random
print("=== Análise de Latência ===")
testes_ping = []
for i in range(0,5):
    teste = random.randint(1,500)
    testes_ping.append(teste)
print(f"O tempo de resposta dos 5 testes de ping em milissegundos foi {testes_ping}, respectivamente.")

maior = max(testes_ping)
menor = min(testes_ping)
media = sum(testes_ping)/len(testes_ping)
print(f"O maior tempo de latência foi {maior} ms, o menor tempo foi de {menor} ms. A média resultou em {media} ms.")
