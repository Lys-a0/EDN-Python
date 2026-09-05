def calculadora(opcao, n1, n2):
    if opcao == "1":
        return n1 + n2
    elif opcao == "2":
        return n1 - n2
    elif opcao == "3":
        return n1 * n2
    elif opcao == "4":
        return n1 / n2
    else:
        return ("\nOpção inválida!")

print("=" * 30)
print("        CALCULADORA")
print("=" * 30)
print("Escolha uma operação: \n 1 - Soma (+) \n 2 - Subtracao(-) \n 3 - Multiplicao(*) \n 4 - Divisão (/)")
opcao = input("\nDigite o numero da operação: ")

n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

resultado = calculadora(opcao, n1, n2)
print(f"\nResultado: {resultado}")