print("=== Cadastro Modular ===")
emails_validos = ("@gmail.com", "@yahoo.com", "@hotmail.com")

def cadastrar_nome():
    nome = input("Digite o seu nome: ").capitalize()
    print("Nome cadastrado.")
    return nome

def cadastrar_email():
    opcao = int(input("\nVocê já possui e-mail (Aceitamos somente Gmail, Yahoo ou Hotmail)? (0 = Sim; 1 = Não): "))
    while opcao != 0 and opcao != 1:
        print("Opção inválida. Digite 0 para 'Sim' e 1 para 'Não.")
        opcao = int(input("Você já possui e-mail (Aceitamos somente Gmail, Yahoo ou Hotmail)? (0 = Sim; 1 = Não): "))
    if opcao == 0:
        return pedir_email_valido(emails_validos)
    else:
        return criar_email()

def pedir_email_valido(emails_validos):
    email = input("Digite seu email: ")
    while not email.endswith(emails_validos):
        print(f"E-mail inválido. Termine seu e-mail com {', '.join(emails_validos)}")
        email = input("Digite seu email: ")
    print("Email cadastrado.")
    return email

def criar_email():
    print("Sem problemas. Auxiliaremos-te a criar um novo e-mail!")
    email = input("Digite um e-mail com final '@fake.com': ")
    while not email.endswith("@fake.com"):
        print("E-mail inválido. Termine seu e-mail com '@fake.com'")
        email = input("Digite um e-mail com final '@fake.com': ")
    print("Email cadastrado.")
    return email

def validar_idade():
    idade = int(input("\nDigite sua idade em anos completos: "))
    if idade >= 18:
        validacao = "Maior de idade"
    else:
        validacao = "Menor de Idade"
    return idade, validacao

print("Seja Bem-vindo ao site Kamilly Deusa Linda ♡")
nome = cadastrar_nome()
email = cadastrar_email()
idade, validacao = validar_idade()

print("\n=== Cadastro final ===")
print(f"Nome: {nome}", f"\nE-mail: {email}", f"\nIdade: {idade}", f"\nVocê é {validacao}")
