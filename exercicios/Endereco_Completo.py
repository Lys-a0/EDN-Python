#  Crie três variáveis: cidade, estado e cep. Peça ao usuário para preencher cada uma e, ao final, exiba o endereço formatado em uma única linha.

cep = input("Digite seu CEP: ")
cidade = input("Digite a cidade: ")
estado = input("Digite o Estado: ")
print ("Seu endereço está Localizado no cep {}, na Cidade de {} no Estado do {}". format(cep, cidade,estado))

