# print(2 + 2 < 4)

# b = ((7//3) == 1+1)
# print(b)

# c = (3**2) + (4**2) == 25
# print (c)

# d = (2 + 4 + 6) > 12
# print(d)

# print(1387 % 19 == 0)

# print(31%2 == 0)

# print(min(34, 29, 31) < 30)

# idade = int(input("Digite sua idade: "))
# if(idade > 60):
#     print("Você tem direito aos benefícios")



# dano = int(input("Digite o dano: "))
# escudo = int(input("Digite o valor do escudo: "))
# if(dano>10 and escudo == 0):
#     print("Você está morto")

# norte = False
# sul = False
# leste = False
# oeste = True
# if (norte or sul or leste or oeste):
#     print("Você escapou")


# ano = int(input("Digite um ano: "))
# if (ano%4 == 0):
#     print("Pode ser um ano bissexto")
# else:
#     print("Definitivamente não é um ano bissexto")


# cima = input("Cima: ")
# baixo = input("Baixo: ")

# if(cima and baixo):
#     print("Decida-se!")
# else:
#     print("VocÊ escolheu um caminho!")


# lado1 = int(input("Digite o valor do lado1: "))
# lado2 = int(input("Digite o valor do lado2: "))
# lado3 = int(input("Digite o valor do lado3: "))

# if(lado1 == lado2 and lado1 == lado3):
#     print("Triangulo equilátero")
# elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
#     print("Triangulo Isósceles")
# else:
#     print("Triangulo Escaleno")



print("CALCULADORA")
print("+ Adição")
print("- Subitração")
print("* Multiplicação")
print("/ Divisão")
print("Pressione outra tecla para sair")

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
else:
    print("Operação Cancelada.")

   
    
# print(" ")
# print("CONTA DE LUZ")

# print("Tipos de instalação:")
# print("R para Residência")
# print("I para Indústria")
# print("C para Comércio")
# tipo = input("Selecione o tipo de instalação (R, C ou I): ")

# if(tipo == "R" or tipo == "I" or tipo == "C"):
#     energiaConsumida = float(input("Digite o consumo de energia elétrica (kWh) do estabelecimento: "))
#     if(tipo == "R"):
#         if(energiaConsumida <= 500):
#             valorAPagar = energiaConsumida*0.4
#         else:
#             valorAPagar = energiaConsumida*0.65
#     elif(tipo == "I"):
#         if(energiaConsumida <= 1000):
#             valorAPagar = energiaConsumida*0.55
#         else:
#             valorAPagar = energiaConsumida*0.6
#     elif(tipo == "C"):
#         if(energiaConsumida <= 5000):
#             valorAPagar = energiaConsumida*0.55
#         else:
#             valorAPagar = energiaConsumida*0.6
            
#     print("Tipo de instalação: {} / Consumo em KWh: {} / Valor a ser pago: {} reais".format(tipo,energiaConsumida, valorAPagar))

# print("Programa finalizado")



