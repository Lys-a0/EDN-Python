# Pedir duas notas, calular a media e dizer se o aluno esta aprovad (média ≥ 7)


# ENTRADA
print("="*30)
print("      SISTEMA DE MÉDIAS")
print("="*30)
n1 = float(input("\nDigite a primeira nota: "))
n2 = float(input("Digite a primeira nota: "))

# CÁLCULO DA MÉDIA
media = (n1 + n2) / 2

# SAÍDA E VERIFICAÇÃO
print("\n" + "="*30)
print("Média: {:.1f}".format(media)) #{:.1f} formatação p/ nª decimal com 1 casa após vírgula

if media >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")
print("="*30)