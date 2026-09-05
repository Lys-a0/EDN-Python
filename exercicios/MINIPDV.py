def ler_texto(mensagem):
    try:
        return input(mensagem)
    except OSError:
        print("\nErro: este ambiente não permite entrada de dados pelo teclado.")
        return ""


def ler_float(mensagem):
    while True:
        try:
            return float(ler_texto(mensagem))
        except ValueError:
            print("Digite um valor válido. Exemplo: 10.50")


def ler_int(mensagem):
    while True:
        try:
            return int(ler_texto(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")


print("=" * 40)
print("   MINI PDV - PONTO DE VENDA")
print("=" * 40)

total = 0
itens = []

while True:
    print("\n--- NOVO ITEM ---")

    produto = ler_texto("Nome do produto: ")

    if produto == "":
        print("Cadastro encerrado.")
        break

    preco = ler_float("Preço do produto: R$ ")

    total = total + preco
    itens.append((produto, preco))

    print("Produto cadastrado:", produto)

    continuar = ler_texto("\nDeseja adicionar mais itens? (s/n): ")

    if continuar.lower() != "s":
        break
desconto = 0

if total > 100:
    desconto = total * 0.10
    mensagem_desconto = "Parabéns! Você recebeu 10% de desconto."
else:
    mensagem_desconto = "Esta compra não possui desconto."

total_final = total - desconto


print("\n" + "=" * 40)
print("       FORMAS DE PAGAMENTO")
print("=" * 40)

print("1 - DINHEIRO")
print("2 - PIX")
print("3 - CARTÃO")

while True:
    opcao = ler_texto("\nEscolha a forma de pagamento: ")

    if opcao == "1":
        forma = "DINHEIRO"
        break

    elif opcao == "2":
        forma = "PIX"
        break

    elif opcao == "3":
        forma = "CARTÃO"

        while True:
            parcelas = ler_int("Deseja parcelar em quantas vezes? (1 a 3): ")

            if parcelas >= 1 and parcelas <= 3:
                valor_parcela = total_final / parcelas
                break
            else:
                print("Número de parcelas inválido! Escolha de 1 a 3.")

        break

    else:
        print("Opção inválida! Tente novamente.")


print("\n" + "=" * 40)
print("          RESUMO DA COMPRA")
print("=" * 40)

if len(itens) == 0:
    print("Nenhum item foi comprado.")
else:
    print("\nItens Comprados:")

    for item, (produto, preco) in enumerate(itens, 1):
        print(f"{item}. {produto:20} - R$ {preco:8.2f}")

print("-" * 40)
print(f"Total da compra: R$ {total:.2f}")
print(mensagem_desconto)
print(f"Desconto:        R$ {desconto:.2f}")
print(f"Valor final:     R$ {total_final:.2f}")
print("-" * 40)

print(f"Forma de pagamento: {forma}")

if forma == "CARTÃO":
    print(f"Parcelamento: {parcelas}x de R$ {valor_parcela:.2f}")

print("=" * 40)
print("       OBRIGADO PELA COMPRA!")
print("=" * 40)

# Extensão: Pesquisa de Satisfação
participar = input("\nGostaria de participar da nossa pesquisa de satisfação? (s/n): ").lower()

if participar == 's':
    print("\nFicamos felizes em ouvir você!")

    # Validação da nota
    while True:
        try:
            nota = int(input("De 0 a 10, como você avalia nosso atendimento hoje? "))
            if 0 <= nota <= 10:
                break
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, use apenas números inteiros.")

    comentario = input("Gostaria de deixar um breve comentário para melhorarmos sua experiencia? (Opcional): ")

    print("\nObrigado! Agradecemos o seu feedback para melhorarmos sempre.")
else:
    print("\nSem problemas. Agradecemos a preferência e esperamos te ver em breve!")