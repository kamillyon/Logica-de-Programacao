import time
print("=== Monitoramento de CPU ===")
porcentagem = 0
while porcentagem < 100:
    porcentagem += 10
    print(f"{porcentagem}%")
    time.sleep(1)