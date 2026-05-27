print("=== Filtro de Domínios em E-mails ===")
emails = ["teste@gmail.com", "admin@escola.br", "prof@escola.br", "bla@fake.com", "nhe@yahoo.com"]
print("Exibiremos os e-mails cadastrado no nosso servidor de domínio '@escola.br'")
for email in emails:
    if email.endswith("@escola.br"):
        print(f"- {email}")