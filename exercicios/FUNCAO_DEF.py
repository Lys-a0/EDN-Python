# Crie um programa que pergunte: nome do aluno, idade, se está matriculado (True ou False),
# mostre tudo organizado

def cadastro(aluno, idade, matricula):
    if matricula == "true":
        status = "Matriculado(a)"
    else:
        status = "Não Matriculado(a)"
    return f"\nSTATUS: O Aluno(a) {aluno} de {idade} anos, matriculado: {status}"

print("\n==== SISTEMA DE ALUNOS ====\n")
aluno = input("Nome do aluno(a): ")
idade = input("Idade: ")
matricula = input("Está matriculado(a)? (true/false): ")

resultado = cadastro(aluno, idade, matricula)
print(resultado)


print("\n")
print("*"*100)
# Crie um programa que pergunte: Nome, ano do nascim., usar o ano atual como constante, calcular e mostrar idade

def dados(nome, ano_nasc, ano_atual):
    idade = ano_atual - ano_nasc
    return f"{nome}, você tem {idade} anos em {ano_atual}"

print("\n=== CALCULADORA DE IDADE ===\n")
nome = input ("Nome: ")
ano_nasc = int(input("Ano de Nacimento: "))
ano_atual = 2026

resultado = dados(nome, ano_nasc, ano_atual)
print(resultado)


print("\n")
print("*"*100)
# Peça dois números ao usuário e mostre: soma, subtracao, multiplicacao e divisao
def calculadora(opcao, n1, n2):
    if opcao == "1":
        return n1 + n2
    elif opcao == "2":
        return n1 - n2
    elif opcao == "3":
        return n1 * n2
    elif opcao == "4":
        return n1 / n2
    else:
        return ("\nOpção inválida!")

print("=" * 30)
print("        CALCULADORA")
print("=" * 30)
print("Escolha uma operação: \n 1 - Soma (+) \n 2 - Subtracao(-) \n 3 - Multiplicao(*) \n 4 - Divisão (/)")
opcao = input("\nDigite o numero da operação: ")

n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

resultado = calculadora(opcao, n1, n2)
print(f"\nResultado: {resultado}")


print("\n")
print("*"*100)
# Verificar se o numero é par

def verificar_par(n):
    return n % 2 == 0

print ("\n=== O NÚMERO É PAR? ===")
n = int(input("Digite um número: "))

if verificar_par(n):
    print(f"O número {n} é PAR.")
else:
    print(f"O número {n} é ÍMPAR.")

resultado = verificar_par(n)

print("\n")
print("*"*100)

# Crie um programa que pergunte: Nome do aluno,Idade,Três notas,Calcule a média.
# Verifique: Se é maior de idade, Se a média é par ou ímpar, Se está aprovado (média ≥ 7)
# Mostre tudo organizado na tela

print("="*30)
print("      SISTEMA DE ALUNOS")
print("="*30)

#ENTRADA DOS DADOS: NOME e IDADE
def dados_alunos():                                  # ← Sem parâmetros
    name = input("Nome do aluno(a): ")
    idade = int(input("Idade: "))
    return name, idade

# SOLICITAR 3 NOTAS
def obter_notas():
    print("=" * 30)
    print("      Nota do Aluno")
    print("=" * 30)
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    return n1, n2, n3

# Verificar se é maior de idade
def verificar_maior_idade(idade):
    if idade >= 18:
        return "SIM"
    else:
        return "NÃO"

#CALCULO MEDIA DAS NOTAS
def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

#VERIFICAR MEDIA SE É IMPAR OU PAR
def verificar_par_impar(media):
    if media % 2 == 0:
        return "PAR"
    else:
        return "IMPAR"

# Verificar se está aprovado
def verificar_aprovacao(media):
    if media >= 7:
        return "APROVADO"
    else:
        return "REPROVADO"

def exibir_relatorio(name, idade, n1, n2, n3):           #aqui ja se tornam parametros

    media = calcular_media(n1,n2,n3)                     # Calcular media
    maior_idade = verificar_maior_idade(idade)           # verificar maioridade
    par_impar = verificar_par_impar(media)               # Media impar/par
    status = verificar_aprovacao(media)                  # Verificar aprovacao

    print("\n")
    print("="*30)
    print("      RELATÓRIO DO ALUNO")
    print("="*30)

    print(f"Aluno: {name}")
    print(f"Idade: {idade} anos")
    print(f"Maior de idade: {maior_idade}")
    print(f"Notas: {n1} | {n2} | {n3}")
    print(f"\nMédia final: {media:.1f}")
    print(f"Média: {par_impar}")
    print(f"Status: {status}")
    print("=" * 30)

# chamada de informações do programa principal
name, idade = dados_alunos()
n1, n2, n3 = obter_notas()
exibir_relatorio(name, idade, n1, n2, n3)
