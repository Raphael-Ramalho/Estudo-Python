
# def fatorial(num):
#     """
#     funcao para calcular fatorial
#     : param num: valor inteiro opicional 
#     : return: resposta do fatorial 
#     """
#     fat = 1
#     if (num == 0):
#         return fat
#     for i in range (1, num+1, 1):
#         fat = fat*i
#     return fat

# def valida_int(pergunta, min, max):
#     num = int(input(pergunta))
#     while (num < min) or (num > max):
#         num = int(input(pergunta))
#     return num
        
# x = valida_int("Digite um valor para calcular o fatorial: ", 0, 50)
# print(fatorial(x))



def valida_int(pergunta, min, max):
    num = int(input(pergunta))
    while (num < min) or (num > max):
        num = int(input(pergunta))
    return num

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#Programa principal
arquivo = "games.txt"
if existeArquivo(arquivo):
    print("Arquivo localizado no computador")
else:
    print("Arquivo inexistente")

while True:
    print("Menu")
    print("1 - Cadastrar novo item")
    print("2 - Listar cadastros")
    print("3 - Sair")

    op = valida_int("Escolha a opção desejada", 1, 3)

    if op == 1:
        print("opção de cadastrar novo item selecionado...\n")
    elif op == 2:
        print("Opção de listar selecionada...\n")
    elif op == 3:
        print("Encerrando o programa...")
        break
