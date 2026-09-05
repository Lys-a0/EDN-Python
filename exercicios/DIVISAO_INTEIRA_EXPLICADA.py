# Pedir 1 numeros e mostrar: Divisão inteira, resto da divisao e explicar com comentarios

#ENTRADA DE DADOS:
print("="*50)                 # pegar o caracter dentro das aspas e repetir 50 vezes
print("              DIVIDÃO INTEIRA E RESTO")
print("="*50)

# Solicitar os numeros e converter para inteiro
n1 = int(input("Digite o segundo número: "))
n2 = int(input("Digite o segundo número: "))

# Explicação do operador // (divisão inteira)
print("\n*** OPERADOR // (DIVISÃO INTEIRA) ***")
divisao_int = n1 // n2
print("   --> {} // {} = {}".format(n1, n2, divisao_int))
print("Este operador retorna APENAS a parte inteira da divisão.")
print("Ignorando as casas decimais (o resto).")

# Explicação do operador % (resto)
print("\n*** OPERADOR % (RESTO DA DIVISÃO) ***")
resto = n1 % n2
print("   --> {} % {} = {}".format(n1, n2, resto))
print("Este operador retorna o que SOBRA da divisão.")
print("É o resto que não foi possível dividir igualmente.")

# RESULTADOS FINAIS
print("\n" + "="*50)
print("         *** RESULTADOS FINAIS: *** ")
print("="*50)
print("   Divisão inteira: {} // {} = {}".format(n1, n2, divisao_int))
print("   Resto da divisão: {} % {} = {}".format(n1, n2, resto))
