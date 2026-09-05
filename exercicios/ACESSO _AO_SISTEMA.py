# Pergunte ao usuário: Se está logado, se é administrador, virificar se pode acessar o sistema

print("="*30)
print("      CONTROLE DE ACESSO")
print("="*30)

# ENTRADA - (l) logado - (ad) admin
l = input("\nEstá logado? (sim/não): ").lower()      #lower = converte em letras minusculas
ad = input("É administrador? (sim/não): ").lower()

# VERIFICAR ACESSO
print("\n" + "="*30)

if l and ad == "sim":                                 # and = E / combina 2 condições
    print("ACESSO PERMITIDO")
    print("Bem-vindo, Administrador!")
elif l and ad == "não":
    print("ACESSO PERMITIDO")
    print("Bem-vindo, Usuário Comum!")
elif l == "não":
    print("ACESSO NEGADO")
    print("Você precisa estar logado para acessar o sistema!")
else:
    print("RESPOSTA INVÁLIDA")
    print("Digite apenas 'sim' ou 'não'")
print("="*30)

