num = int(input("Digite um número positivo: "))

def fatorial(num = 0):
    """
    funcao para calcular fatorial
    : param num: valor inteiro opicional 
    : return: resposta do fatorial 
    """
    res = 1
    while (num >= 1):
        res *= num
        num -= 1
    return res

def valPositivo(num):
    if(num >= 0):
        return fatorial(num)
    else:
        return "valor invalido"
        

print(valPositivo(num))