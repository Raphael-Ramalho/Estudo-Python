# Qa = 1 + 2 + 3 + 4 + 5
# print(Qa)

# a = 23
# b = 19
# c = 31
# Qb = (a + b + c)/3
# print(Qb)

# Qc = 403//73
# print(Qc)

# Qd = 403 % 73
# print(Qd)

# Qe = 2**10
# print(Qe)

# Qf = abs(54 - 57) 
# print(Qf)

# Qg = min(34, 29, 31)
# print(Qg)



# a = 3
# b = 4
# c = a*a + b*b

# s1 = "ant"
# s2 = "bat"
# s3 = "cod"

# s4 = s1 + " " + s2 + " " + s3
# s5 = (s1 + " ")*10
# s6 = (s1 + " " + s2 + " ")*7
# s7 = (s2*2+s3)*5



# preco = float(input("insira o preço de um produto: "))
# desconto = float(input("insira o percentual de desconto do produto (0-100)%: "))

# valorDesconto = (desconto/100) * preco
# precoFinal = preco - valorDesconto
# print("O desconto foi de {} reais e o valor final do produto é {} reais.".format(valorDesconto, precoFinal))



# kmPercorridos = int(input("Digite a quantidade de kilometros percorridos pelo carro: "))
# custoPorKM = 0.15

# diasAlugados = int(input("O carro foi alugado por quantos dias? "))
# custoDiario = 60

# precoAPagar = (kmPercorridos*custoPorKM)+(diasAlugados*custoDiario)
# print("Valor a ser pago: {} reais.".format(precoAPagar))



stringQualquer = input("Digite uma frase qualquer: ")
metade = stringQualquer[0:int((len(stringQualquer)/2))]
ultimosCaracteres = metade[(len(metade)-2):]
print(metade, ultimosCaracteres)
