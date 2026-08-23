def converter_idade(texto):
    try:
        idade = int(texto)
    except ValueError as erro:

        raise ValueError("Idade deve ser um número inteiro.") from erro

    if not 0 <= idade <= 130:
        raise ValueError("Idade fora da faixa permitida.")
    return idade


for entrada in ("30", "trinta", "200"):
    try:
        print(converter_idade(entrada))
    except ValueError as erro:
        print("Erro:", erro)