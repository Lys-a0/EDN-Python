def dados(nome, ano_nasc, ano_atual):
    idade = ano_atual - ano_nasc
    return f"{nome}, você tem {idade} anos em {ano_atual}"

print("\n=== CALCULADORA DE IDADE ===\n")
nome = input ("Nome: ")
ano_nasc = int(input("Ano de Nacimento: "))
ano_atual = 2026

resultado = dados(nome, ano_nasc, ano_atual)
print(resultado)