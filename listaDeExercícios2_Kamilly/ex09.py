print("=== Monitoramento de Presença ===")
percentual_faltas = float(input("Digite aqui o percentual de faltas acumuladas pelo estudante: "))
if percentual_faltas >= 12.5:
    print("ATENÇÃO: Limite de ausência atingido.")
else:
    print("Frequência regular.")