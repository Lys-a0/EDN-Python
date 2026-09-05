# Permita cadastrar alunos com nome e idade. Armazene os dados em uma lista.
# Exiba um menu com opções:1 → Cadastrar aluno/2 → Listar alunos cadastrados/0 → Sair
# Use variáveis, if/else e laços de repetição para controlar o fluxo.

#INICIO DO SISTEMA
print("="*50)
print("        SISTEMA DE CADASTRO DE ALUNOS")
print("="*50)

#Criar uma lista vazia para armazenar alunos
alunos_lista = []

#CRIAR UM MENU COM OPCOES
print("MENU: ")
print(" 1 - Cadastrar Aluno \n 2 - Listar alunos cadastrados \n 0 - Sair")

opcao = input("Escolha um opção: ")


if opcao == "1":
    print("\n--- CADASTRO DE ALUNO ---")
    nome = input("Nome do aluno: ")
    idade = input("Idade: ")
    alunos.append([nome, idade])
    print(f"Aluno {nome} cadastrado com sucesso!")
# todo: Aplicar condição para repeticao infinita

elif opcao == "2":
    if alunos == []:
        print


