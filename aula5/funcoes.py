def cabecalho (titulo):
    if titulo:
        bordaSI(titulo)
        print("|{}|".format(titulo))
        bordaSI(titulo)

def bordaSI(titulo):
    numTracos = len(titulo)
    # print("+", "-"*numTracos, "+")
    print("+{}+".format("-"*numTracos))

cabecalho("Ramalho")