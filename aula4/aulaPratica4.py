print("CALCULADORA")
print("+ Adição")
print("- Subitração")
print("* Multiplicação")
print("/ Divisão")
print("Digite 's' para sair")

operacao = 0
while(operacao != "s"):
    operacao = input("Qual operação deseja fazer? ")
    
    if(operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/"):
        v1 = float(input("Digite o primeiro valor: "))
        v2 = float(input("Digite o segundo valor: "))

        if(operacao == "+"):   
            v3 = v1 + v2
            print("{} + {} = {}".format(v1, v2, v3))
        elif(operacao == "-"):
            v3 = v1 - v2
            print("{} - {} = {}".format(v1, v2, v3))
        elif(operacao == "*"):
            v3 = v1 * v2
            print("{} * {} = {}".format(v1, v2, v3))
        elif(operacao == "/"):
            v3 = v1 / v2
            print("{} / {} = {}".format(v1, v2, v3))

    elif(operacao == "s"):
        break

    else:
        print("Operação inválida. Tente novamente.")
        print("+ Adição")
        print("- Subitração")
        print("* Multiplicação")
        print("/ Divisão")
        print("Digite 's' para sair")

print("Programa encerrado.")