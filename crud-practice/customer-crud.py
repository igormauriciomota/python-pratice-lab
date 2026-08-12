"""
CRUD, lista de dicionarios while, menu: cadastrar, listar, buscar, excluir e sair

"""


clientes = []

while True:

    print("\n--- ESCOLHA UMA OPÇÃO ---")
    print(" 1 - Cadastrar")
    print(" 2 - Listar")
    print(" 3 - Buscar")
    print(" 4 - Excluir")
    print(" 0 - Sair")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        cliente = {
            "nome": input("Nome: ").strip().capitalize(),
            "email": input("E-mail: ").strip()
        }

        clientes.append(cliente)
        print("Cliente cadastrado.")

    elif opcao == "2":
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. {cliente['nome']} - {cliente['email']}")

    elif opcao == "3":
        nome = input("Nome para buscar: ").strip().lower()
        encontrado = False
        for cliente in clientes:
            if cliente["nome"].lower() == nome:
                print(cliente)
                encontrado = True
                break

        if not encontrado:
            print("Cliente não encontrado.")

    elif opcao == "4":
        nome = input("Nome para excluir: ").strip().lower()
        for cliente in clientes:
            if cliente["nome"].lower() == nome:
                clientes.remove(cliente)
                print("Cliente Excluido.")
                break
        else:
            print("Cliente não encontrado.")

    elif opcao == "0":
        break
    else:
        print("Opção invalida.")

print("Fim do Programa")