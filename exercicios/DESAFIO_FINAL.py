# Crie um programa que pergunte: Nome do aluno,Idade,Três notas,Calcule a média.
# Verifique: Se é maior de idade, Se a média é par ou ímpar, Se está aprovado (média ≥ 7)
# Mostre tudo organizado na tela

#ENTRADA DOS DADOS: NOME e IDADE
print("="*30)
print("      SISTEMA DE ALUNOS")
print("="*30)
aluno = input ("Nome do aluno(a): ")
idade = int(input ("Idade: "))

# SOLICITAR 3 NOTAS
print("="*30)
print("      Nota do Aluno")
print("="*30)
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

print("\n")
print("="*30)
print("      RELATÓRIO DO ALUNO")
print("="*30)
print("Nome do aluno: {}".format(aluno))
print("Idade: {} anos".format(idade))

# Verificar se é maior de idade
if idade >= 18:
    print("Maior de idade: SIM")
else:
    print("Maior de idade: NÃO")

#CALCULO MEDIA e SE É IMPAR OU PAR
media = (n1 + n2 + n3) / 3
print("\nNota total: {:.1f}".format(media))

# Verificar se a média é par ou ímpar
if media % 2 == 0:
    print("\nMédia: PAR")
else:
    print("\nMédia: ÍMPAR")

# Verificar se está aprovado
if media >= 7:
    print("Stats: APROVADO")
else:
    print("Status: Reprovado")
print("="*30)

