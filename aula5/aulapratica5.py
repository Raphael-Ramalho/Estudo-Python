
def fatorial(num):
    """
    funcao para calcular fatorial
    : param num: valor inteiro opicional 
    : return: resposta do fatorial 
    """
    fat = 1
    if (num == 0):
        return fat
    for i in range (1, num+1, 1):
        fat = fat*i
    return fat

def valida_int(pergunta, min, max):
    num = int(input(pergunta))
    while (num < min) or (num > max):
        num = int(input(pergunta))
    return num
        
x = valida_int("Digite um valor para calcular o fatorial: ", 0, 50)
print(fatorial(x))