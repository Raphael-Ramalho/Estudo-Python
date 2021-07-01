from typing import final


# a = int(input("Qual valor deseja iniciar a contagem? "))
# b = int(input("Qual valor deseja finalizar a contagem?"))
# while(a <= b):
#     if(a % 2 == 0):
#         print(a)
#     a = a + 1


# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# n3 = float(input("Nota 3: "))
# n4 = float(input("Nota 4: "))
# n5 = float(input("Nota 5: "))

# media = (n1 + n2 + n3 + n4 + n5)/5

# x=[]
# i=0
# total = 0
# numNotas = 5
# while(i<=(numNotas-1)):
#     x.append(float(input("Nota {}: ".format(i+1))))
#     total = total + x[i]
#     i=i+1
# media = total/numNotas
# print(media)

print("Digite 'sair' para sair do programa")
x = " "
while(x != "sair"):
    x = input("Digite uma palavra: ")
    print(x)
print("Programa finalizado!")
