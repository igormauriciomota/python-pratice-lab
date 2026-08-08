# Importa o modulo inteiro

import calculadora

continuar = True

while continuar:

    print("\n === Calculadora Simples === ")

    numero1 = float(input("\nDigite o primeiro número: "))
    numero2 = float(input("\nDigite o segundo número: "))

    print("\nEscolha a operação:")
    print(" +  Soma")
    print(" -  Subtração")
    print(" *  Multiplicação")
    print(" /  Divisão")

    operacao = input("\nDigite a operação desejada (+, -, *, /): ")

    if operacao == "+":
        resultado = calculadora.soma(numero1, numero2)
        
    elif operacao == "-":
        resultado = calculadora.subtracao(numero1, numero2)
        
    elif operacao == "*":
        resultado = calculadora.multiplicacao(numero1, numero2)
        
    elif operacao == "/":
        resultado = calculadora.divisao(numero1, numero2)

        if resultado is None:
            print("Erro: Divisão por zero!")

        
    else:
        print("Operação inválida!")

    if resultado is not None:
        print(f"\nResultado: {resultado}")

    continuar = input("\nDeseja realizar outra operação? (s/n): ").lower() == "s"

print("\nObrigado por usar a calculadora!")
