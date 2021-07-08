print("\nExercicio 1")
print("Digite o nome e a nota do aluno para receber seu conceito")

while True:
    dados = int(input("Inserir dados? (0 - Não / 1 - Sim) ")) #Usuário digita 1 para usar o programa ou 0 para finaliza-lo.
    if dados: 
        #Esse bloco é acessado se a variavel "dados" tiver valor diferente de 0. 
        nome = input("Nome do aluno: ")
        while True:
            notaFinal = float(input("Nota final: "))
            if (notaFinal < 0): #Se a nota final digitada for negativa, o print desse bloco é executado e o laço while é reiniciado, forçando o usuário a digitar um novo valor para a nota final.
                print("Valor inválido. Digite novamente...")
                continue
            elif(notaFinal <= 2.9): #Bloco acessado se a nota final for positiva e inferior ou igual a 2,9.
                print("O(A) aluno(a) {} tirou a nota {} e se enquadra no conceito E".format(nome, notaFinal))
                break
            elif(notaFinal <= 4.9): #Bloco acessado se a nota final for superior a 2,9 e inferior ou igual a 4,9.
                print("O(A) aluno(a) {} tirou a nota {} e se enquadra no conceito D".format(nome, notaFinal))
                break
            elif(notaFinal <= 6.9): #Bloco acessado se a nota final for superior a 4,9 e inferior ou igual a 6,9.
                print("O(A) aluno(a) {} tirou a nota {} e se enquadra no conceito C".format(nome, notaFinal))
                break
            elif(notaFinal <= 8.9): #Bloco acessado se a nota final for superior a 6,9 e inferior ou igual a 8,9.
                print("O(A) aluno(a) {} tirou a nota {} e se enquadra no conceito B".format(nome, notaFinal))
                break
            elif(notaFinal <= 10): #Bloco acessado se a nota final for superior a 8,9 e inferior ou igual a 10.
                print("O(A) aluno(a) {} tirou a nota {} e se enquadra no conceito A".format(nome, notaFinal))
                break
            else: #Bloco acessado se a nota final for superior a 10, ou seja, um valor invalido.
                print("Valor inválido. Digite novamente...")
                continue
    else:
        #Bloco acessado se a variavel "dados" tiver o valor 0.
        print("Fim do programa...")
        break
    


