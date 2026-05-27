print("=== Alerta de Temperatura ===")
temp_celsius = float(input("Digite a temperatura atual do seu servidor em graus Celsius: "))
if temp_celsius > 75:
    print("ALERTA: Superaquecimento!!")
else:
    print("Temperatura normal.")