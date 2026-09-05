# Crie um programa que pergunte: nome do aluno, idade, se está matriculado (True ou False), mostre tudo organizado

#ENTRADA DE DADOS:
print("\n\n==== SISTEMA DE ALUNOS ====\n")
aluno = input ("Nome do aluno(a): ")
idade = input ("Idade: ")
matricula = input ("Está matriculado(a)? (true/false): ")

#ESTRUTURA IF/ELSE e SAIDA
if matricula == "true":
    status = "Matriculado(a)"
else:
    status = "Não Matriculado(a)"

print ("\nSTATUS: O Aluno(a) {} de {} anos, matriculado: {}".format(aluno, idade, status))
