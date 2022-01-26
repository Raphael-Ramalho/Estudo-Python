
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

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "wt+")
        a.close()
    except:
        print("erro na criação do arquivo")
    else:
        print("Arquivo {} foi criado com sucesso!\n".format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo): 
    try:
        a = open(nomeArquivo, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, "at")
    except:
        print("Erro ao abrir o arquivo")
    else:
        a.write("{};{}\n".format(nomeJogo,nomeVideogame))
    finally:
        a.close()

#Programa principal
arquivo = "games.txt"

if existeArquivo(arquivo):
    print("Arquivo localizado no computador")
else:
    print("Arquivo inexistente")
    criaArquivo(arquivo)

while True:
    print("Menu")
    print("1 - Cadastrar novo item")
    print("2 - Listar cadastros")
    print("3 - Sair")

    op = valida_int("Escolha a opção desejada: ", 1, 3)

    if op == 1:
        print("opção de cadastrar novo item selecionado...\n")
        nomeJogo = input("Nome do jogo:")
        nomeVideogame = input("Nome do videogame:")
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print("Opção de listar selecionada...\n")
        listarArquivo(arquivo)
    elif op == 3:
        print("Encerrando o programa...")
        break

