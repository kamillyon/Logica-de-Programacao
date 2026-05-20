import time
print("=== Lista de Dsenvolvedores ===")
desenvolvedores = ["Ada Lovelace", "Dennis Ritchie", "Ken Thompson", "Margaret Hamilton", "Grace Hopper"]
indice = 0
while indice < len(desenvolvedores):
    print(desenvolvedores[indice])
    indice += 1
    time.sleep(1)