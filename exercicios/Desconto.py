# Crie um programa, cuja função: Receba um valor em Reais e Retorne o valor com 15% de imposto.
# 15% de imposto.

# TODO: nomes das variaveis para imposto


# Passo 1: adicionar função
def ap_desconto(valor):             # aplicar desconto
    imposto = valor * 1.15         # 15% de imposto.
    valor_desconto = valor + desconto
    return valor_desconto

# INICIO SISTEMA
print("="*30)
print("      CALCULAR DESCONTO")
print("="*30)

#Passo 2: Interação e aplicar a função
preco = float(input("Digite o valor em Reais: R$ "))
resultado = ap_desconto(preco)

print(f"\nValor com 15% de desconto: R$ {resultado}") #todo: acrescentar em resultado o comando para decimal
print("="*30)
