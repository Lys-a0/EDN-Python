# Peça dois números ao usuário e mostre: soma, subtracao, multiplicacao e divisao

#Entrada - FAZER O USUARIO ESCOLHER UMA OPERAÇÃO
print("="*30)
print("        CALCULADORA")
print("="*30)

print("Escolha uma operação: \n 1 - Soma (+) \n 2 - Subtracao(-) \n 3 - Multiplicao(*) \n 4 - Divisão (/)")
opcao = input("\nDigite o numero da operação: ")

#Adicionar os números para calculo
n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

#ESTRUTURA IF, ELIF, ELSE

if opcao == "1":
    resultado = n1 + n2
    print("\n{} + {} = {}". format(n1, n2, resultado))
elif opcao == "2":
    resultado = n1 - n2
    print("\n{} + {} = {}". format(n1, n2, resultado))
elif opcao == "3":
    resultado = n1 * n2
    print("\n{} + {} = {}". format(n1, n2, resultado))
elif opcao == "4":
    resultado = n1 / n2
    print("\n{} + {} = {}".format(n1, n2, resultado))
else:
    print("\nOpção inválida!")

