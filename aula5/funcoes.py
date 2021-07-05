# def cabecalho (titulo):
#     if titulo:
#         bordaSI(titulo)
#         print("|{}|".format(titulo))
#         bordaSI(titulo)

# def bordaSI(titulo):
#     numTracos = len(titulo)
#     # print("+", "-"*numTracos, "+")
#     print("+{}+".format("-"*numTracos))

# cabecalho("Ramalho")


def imprimeComCondicao(num, fcond):
    if(fcond(num)):
        print(num)

def par(x):
    return x % 2 == 0 
def impar(x):
    return not par(x)

imprimeComCondicao(4,par)