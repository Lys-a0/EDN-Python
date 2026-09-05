def verificar_par(n):
    return n % 2 == 0

print ("\n=== O NÚMERO É PAR? ===")
n = int(input("Digite um número: "))

if verificar_par(n):
    print(f"O número {n} é PAR.")
else:
    print(f"O número {n} é ÍMPAR.")

resultado = verificar_par(n)
