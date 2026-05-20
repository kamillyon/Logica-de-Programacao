print("=== Busca em Lista ===")
usuarios = ["Ada Lovelace", "Dennis Ritchie", "Ken Thompson", "Margaret Hamilton", "Grace Hopper"]

print("Digite um nome e procuraremos se ele é um usuário cadastrado no nosso sistema.")
nome = input("Digite aqui o nome: ")
if nome in usuarios: print("Usuário cadastrado.")
else: print("Usuário não cadastrado.", "\nCadastre-se no nosso sistema.")