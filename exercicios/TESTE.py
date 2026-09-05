#=== INICIALIZAÇÃO DE VARIÁVEIS ===
total_bruto = 0.0

print("=" * 40)
print("          MINI PDV - CAIXA          ")
print("=" * 40)

#=== ESTRUTURA DE REPETIÇÃO (REGISTRO DE PRODUTOS) ===
while True:
    # 1. Pergunta o nome e o preço do produto
    produto = input("\nNome do produto: ")
    preco = float(input(f"Preço de '{produto}' (R$): "))

    # Acumula o preço do produto no total
    total_bruto += preco

    # 2. Pergunta se o usuário quer continuar
    continuar = input("Deseja adicionar mais itens? (S/N): ").strip().upper()

    # Se a resposta for diferente de 'S', quebra o laço de repetição
    if continuar != 'S':
        break

#=== PROCESSAMENTO DO DESCONTO (REGRA DE NEGÓCIO) ===
#Se o valor total for maior que R$ 100,00, aplica 10% de desconto
desconto = 0.0
if total_bruto > 100.00:
    desconto = total_bruto * 0.10

total_com_desconto = total_bruto - desconto

#=== EXIBIÇÃO DO CUPOM FISCAL ===
print("\n" + "=" * 40)
print("             CUPOM FISCAL             ")
print("=" * 40)
print(f"Total Bruto:       R$ {total_bruto:.2f}")

if desconto > 0:
    print(f"Desconto (10%):   -R$ {desconto:.2f}")
    print("-" * 40)
    print(f"TOTAL A PAGAR:     R$ {total_com_desconto:.2f}")
else:
    print("-" * 40)
    print(f"TOTAL A PAGAR:     R$ {total_bruto:.2f}")

print("=" * 40)
print("       OBRIGADO PELA COMPRA!        ")