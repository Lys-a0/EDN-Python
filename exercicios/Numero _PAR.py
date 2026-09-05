# Verificar se o numero é par

#Entrada
print ("\n=== O NÚMERO É PAR? ===")
n = int(input("Digite um número: "))
r = n % 2
print("O resultado é {}". format(r))

#Verificar se é PAR
if r == 0:
    print("O número {} é PAR.".format(n))
else:
    print("O número {} não é PAR.".format(n))