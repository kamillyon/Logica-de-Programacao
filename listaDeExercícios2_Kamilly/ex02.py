print("=== Tempo de Dowload ===")
megabytes = int(input("Digite o tamanho do arquivo em Megabytes (MB): "))
megabits_segundo = int(input("Digite a velocidade do link de internet em Megabits por segundo (Mbps): "))
tempo_dowload = (megabytes*8)/megabits_segundo
print(f"O dowload do seu arquivo de {megabytes} MB demorará {tempo_dowload} segundos")