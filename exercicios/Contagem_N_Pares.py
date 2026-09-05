# Escreva um programa que receba um numero N
# e conte quantos números pares existem de 1 até N.

print("%"*45)
print("     QUANTOS NªPARES EXISTEM DE 1 ATÉ N ")
print("%"*45)
N = int(input("Digite um número N: "))

contador = 0
for i in range(1, N + 1):                   #laço for
    if i % 2 == 0:
        contador +=1

print(f"\nDe 1 até {N}, existem {contador} números pares. ")
print("%"*45)