import math
import statistics
import random

# notas = [9,7,7,10,3,9,6,6,2]

# #print(notas.count(7))

# notas[-1] = 4

# def maiorFunction (notas):
#     maiorNota = 0
#     i = 0
#     while (i < len(notas)):
#         if (maiorNota < notas[i]):
#             maiorNota = notas[i]
#         i += 1
#     return maiorNota

# def media (notas):
#     mediaNotas = statistics.mean(notas)
#     return mediaNotas


# maiorNota = maiorFunction(notas)
# print("Maior nota: {}".format(maiorNota))

# notasOrdenadas = sorted(notas)
# print("Notas Ordenadas: {}".format(notasOrdenadas))

# mediaNotas = media(notas)
# print("Media: {}".format(mediaNotas))



# palavras = ("Mario", "Luigi", "Peach", "Yoshi", "Bowser")

# for palavra in  palavras: 
#     print("\nPalavra : {}. Vogais: ".format(palavra.upper()), end = "")
#     for letra in palavra:
#         if letra.lower() in "aeiou":
#             print(letra.upper(), end = " ")


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x



#Programa principal
print("JOKENPO")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int("Escolha sua jogada: ", 0, 3)
    if not j1:
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    print(jogadas)
