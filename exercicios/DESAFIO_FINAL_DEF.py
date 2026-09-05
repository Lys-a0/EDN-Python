
print("="*30)
print("      SISTEMA DE ALUNOS")
print("="*30)

#ENTRADA DOS DADOS: NOME e IDADE
def dados_alunos():
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

def exibir_relatorio(name, idade, n1, n2, n3):

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

name, idade = dados_alunos()
n1, n2, n3 = obter_notas()
exibir_relatorio(name, idade, n1, n2, n3)





