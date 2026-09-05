# Escreva um programa que  solicite uma senha e permita até 3 tentativas.
# Se acertar, exiba "Acesso permitido", senao "Bloqueado"

print("="*40)
print("         ACESSO AO SISTEMA")
print("="*40)

senha_correta = "1234"
#No FOR, não considera o ultimo numero, por isso tem que ser 4
for tentativa in range(1,4):
    senha = input(f"Tentativa {tentativa} de 3 - Digite a senha: ")

    if senha == senha_correta:
        print("\n  Acesso permitido!")
        break
    else:
        print("Senha Errada!")
else:
    print("\n   Bloqueado! Número de tentativas excedido. ")