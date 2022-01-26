from operator import itemgetter

print("\nExercício 4")

deposito = [] #Cria o array(lista) que vai receber os dicionarios gerados

while True: #Laço de repetição para criar dicionarios, armazenando-os no array "deposito"
    controlador = int(input("Deseja inserir um novo produto? (0 - Não / 1 - Sim) ")) #A variavel "controlador" verifica se o usuário quer inserir um novo dicionario
    if controlador:
       #Bloco acessado se a variavel receber algum valor diferente de 0 do usuário.
        produto={
            "codigo": int(input("Digite o código do produto: ")), 
            "Estoque": int(input("Digite a quantidade do produto em estoque: ")),
            "Minimo": int(input("Digite a quantidade mínima planejada para o estoque do produto: "))
        }
        deposito.append(produto) #dicionário armazenado no final do array "deposito"
    else:
        #bloco acessado quando o usuário digita 0 no input da variavel "controlador"
        print("Exibição dos produtos em estoque:")
        break

listaOrdenada = sorted(deposito, key=itemgetter('codigo')) #Ordenação das bibliotecas contidas no array "deposito" com base na propriedade "codigo" das bibliotecas

print(listaOrdenada)

