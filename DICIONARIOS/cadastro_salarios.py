"""
Realizar o cadastro de funcionarios com nome, idade, função, salario e buscar a media, salario maximo, salario minimo e total

"""
funcionarios = []

salarios = []

quantidade = int(input("Quantidade de funcionarios deseja cadastrar? "))

for i in range(quantidade):

    funcionario = {
        "nome": input("Nome: ").strip().capitalize(),
        "idade": int(input("Idade: ")),
        "funcao": input("Função: ").strip(),
        "salario": float(input("Salario: R$ "))
    }

    # Adicionar todos os funcionarios e suas carcteristicas da lista
    funcionarios.append(funcionario)

    # Adicionar o salario tembem na lista salarios
    salarios.append(funcionario["salario"])

    print("\n --- FUNCIONARIOS ---")

    for funcionario in funcionarios:
        print(
            f"Nome: {funcionario['nome']} | "
            f"Idade: {funcionario['idade']} | "
            f"Função: {funcionario['funcao']} | "
            f"Salario: R$ {funcionario['salario']}"
        )

soma_salario = sum(salarios)
maior_salario = max(salarios)
menor_salario = min(salarios)
media_salario = soma_salario / len(salarios)

print("\n --- ESTATISTICA SALARIAIS --- ")

print(f"Soma de todos salarios: R$ {soma_salario:,.2f}")
print(f"Maior salario: R$ {maior_salario:,.2f}")
print(f"Menor salario: R$ {menor_salario:,.2f}")
print(f"Media salariais: R$ {media_salario:,.2f}")





