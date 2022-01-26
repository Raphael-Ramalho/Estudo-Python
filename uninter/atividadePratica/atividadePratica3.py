import random

print("\nExercicio 3\n")

listaSorteio = [] #A variavel listaSorteio é um array(lista) que receberá o nome dos doadores a serem sorteados

while True: #Laço de repetição para armazenar o nome dos doadores no array
    controlador = int(input("Deseja inserir uma doação? (0 - Não / 1 - Sim) ")) #A variavel "controlador" verifica se o usuário quer inserir uma nova doação. Se ele não quiser, o laço de repetição é interrompido e o sorteio é iniciado.
    if controlador: 
        #Bloco acessado se a variavel receber algum valor diferente de 0 do usuário.
        nome = input("Digite o nome do doador: ")
        valorDoado = float(input("Digite o valor doado: "))#O valor doado pode conter virgulas, por isso, foi usado o float()
        print("{} doou {}".format(nome, valorDoado))#print do nome do doador e do valor doado
        numDeInsercoes = int(valorDoado // 10) #Converte o valor doado no número de vezes que o nome do doador será inserido no array "listaSorteio". O int() foi usado para transformar o numero float em um número int.
        for i in range(numDeInsercoes): #Esse bloco insere o nome do doador x vezes no array "listaSorteio", referente ao valor doado
            listaSorteio.append(nome)
    else:
        #bloco acessado quando o usuário digita 0 no input da variavel "controlador"
        print("\nInício do Sorteio\n")
        break #interrompe o laço de repetição, dando prosseguimento à execução do código

random.shuffle(listaSorteio) #Embaralha a posição dos itens do array "listaSorteio"

print("Lista do sorteio: {}".format(listaSorteio)) #Imprime a lista com os nomes a serem sorteados (listaSorteio)

nomeSorteado = random.choice(listaSorteio) #seleciona um item aleatório do array "listaSorteio"

print("Nome sorteado: {}".format(nomeSorteado)) #Imprime o nome sorteado

