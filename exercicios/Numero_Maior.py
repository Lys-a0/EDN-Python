# Crie um programa que tenha uma FUNÇÃO: RECEBER 2 valores e RETORNAR o MAIOR deles
#Def: CRIA FUNÇÕES / Evita repetição de cód.

# Passo 1: Criar uma função para receber 2 valores
def maior_numero(n1, n2):                   # não esquecer o ( : ) no final
    return max(n1, n2)                      # return max: retorna o maior valor de uma sequencia

#INICIO SISTEMA
print("*"*30)
print("        MAIOR VALOR")
print("*"*30)

# Passo 2: Criar uma interação
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

resultado = maior_numero(n1, n2)
print(f"\nO maior número é: {resultado}")
print("*"*30)
