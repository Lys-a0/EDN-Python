# Crie um programa que pergunte: Nome, ano do nascim., usar o ano atual como constante, calcular e mostrar idade

#Entrada
print("\n=== CALCULADORA DE IDADE ===\n")
nome = input ("Nome: ")
ano_nasc = int(input("Ano de Nacimento: "))

# Calculo
ano_atual = 2026
idade = ano_atual - ano_nasc

#Saida
print("\n === RESULTADO ===\n")
print("{}, você tem {} anos em {}".format(nome, idade, ano_atual))