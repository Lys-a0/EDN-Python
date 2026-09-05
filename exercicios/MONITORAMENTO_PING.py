# Para monitorar a qualidade do link de internet de uma filia, o sistema de suporte realizou 4
# testes automáticos de resposta de rede (Ping), medidos em milissegundos (ms).

#Crie um programa com duas funções que trabalhem juntas:
#1- A primeira função deve se chamar calcular_media_ping. Ela recebe a lista de testes e retorna a média
#aritmética calculada.

#2. A segunda função deve se chamar avaliar_conexão. Ela recebe o número da média calculado pela primeira função.
#Se a média for menor ou igual a 50ms, ela retorna a mensagem "Conexão Estável".
#Caso contrário, retorna "Aviso: Conexão instável ou sob alta carga".

# Monitorar o ping permite verificar a estabilidade e a velocidade da sua conexão com a internet
# ou com servidores específicos

#Função para calcular a média dos pings
def calcular_media_ping(pings):
    soma = 0
    for valor in pings:
        soma = soma + valor
    media = soma / len(pings) # Quant de elementos
    return media

#Funcao para avaliar a conexão com base na média
def avaliar_conexao(media):
    if media <= 50:
        return "Conexão Estável"
    else:
        return "Aviso: Conexão instável ou sob alta carga"


# Programa
testes = [30, 45, 50, 40] # 4 resultados de ping

media_calculada = calcular_media_ping(testes)
resultado = avaliar_conexao(media_calculada)

print(f"Média dos pings: {media_calculada} ms")
print("Resultado", resultado)