import math
import statistics

notas = [9,7,7,10,3,9,6,6,2]

#print(notas.count(7))

notas[-1] = 4

def maiorFunction (notas):
    maiorNota = 0
    i = 0
    while (i < len(notas)):
        if (maiorNota < notas[i]):
            maiorNota = notas[i]
        i += 1
    return maiorNota

def media (notas):
    mediaNotas = statistics.mean(notas)
    return mediaNotas


maiorNota = maiorFunction(notas)
print("Maior nota: {}".format(maiorNota))

notasOrdenadas = sorted(notas)
print("Notas Ordenadas: {}".format(notasOrdenadas))

mediaNotas = media(notas)
print("Media: {}".format(mediaNotas))

