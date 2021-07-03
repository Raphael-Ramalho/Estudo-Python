# print("CALCULADORA")
# print("+ Adição")
# print("- Subitração")
# print("* Multiplicação")
# print("/ Divisão")
# print("Digite 's' para sair")

# operacao = 0
# while(True):
#     operacao = input("Qual operação deseja fazer? ")

#     if(operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/"):
#         v1 = float(input("Digite o primeiro valor: "))
#         v2 = float(input("Digite o segundo valor: "))

#         if(operacao == "+"):   
#             v3 = v1 + v2
#             print("{} + {} = {}".format(v1, v2, v3))
#             continue
#         elif(operacao == "-"):
#             v3 = v1 - v2
#             print("{} - {} = {}".format(v1, v2, v3))
#             continue
#         elif(operacao == "*"):
#             v3 = v1 * v2
#             print("{} * {} = {}".format(v1, v2, v3))
#             continue
#         elif(operacao == "/"):
#             v3 = v1 / v2
#             print("{} / {} = {}".format(v1, v2, v3))
#             continue

#     elif(operacao == "s"):
#         break

#     else:
#         print("Operação inválida. Tente novamente.")
#         print("+ Adição")
#         print("- Subitração")
#         print("* Multiplicação")
#         print("/ Divisão")
#         print("Digite 's' para sair")

# print("Programa encerrado.")

print("Caixa Eletrônico")
print("Para sair, digite 0")

while (True):
    valor = int(input("insira o valor em R$: "))

    if(valor >= 100):
        nota = 100
        numNotas = valor//nota
        valor = valor - (numNotas*nota)
        if(numNotas == 1):
            print("{} nota de {}".format(numNotas, nota))
        else:
            print("{} notas de {}".format(numNotas, nota))
        if(valor == 0): continue

    if(valor >= 50):
        nota = 50
        numNotas = valor//nota
        valor = valor - (numNotas*nota)
        if(numNotas == 1):
            print("{} nota de {}".format(numNotas, nota))
        else:
            print("{} notas de {}".format(numNotas, nota))
        if(valor == 0): continue

    if(valor >= 20):
        nota = 20
        numNotas = valor//nota
        valor = valor - (numNotas*nota)
        if(numNotas == 1):
            print("{} nota de {}".format(numNotas, nota))
        else:
            print("{} notas de {}".format(numNotas, nota))
        if(valor == 0): continue

    if(valor >= 10):
        nota = 10
        numNotas = valor//nota
        valor = valor - (numNotas*nota)
        if(numNotas == 1):
            print("{} nota de {}".format(numNotas, nota))
        else:
            print("{} notas de {}".format(numNotas, nota))
        if(valor == 0): continue

    if(valor >= 5):
        nota = 5
        numNotas = valor//nota
        valor = valor - (numNotas*nota)
        if(numNotas == 1):
            print("{} nota de {}".format(numNotas, nota))
        else:
            print("{} notas de {}".format(numNotas, nota))
        if(valor == 0): continue

    if(valor >= 1):
        nota = 1
        numNotas = valor//nota
        valor = valor - (numNotas*nota)
        if(numNotas == 1):
            print("{} nota de {}".format(numNotas, nota))
        else:
            print("{} notas de {}".format(numNotas, nota))
        if(valor == 0): continue

    if(valor == 0):
        print("fim do programa")
        break