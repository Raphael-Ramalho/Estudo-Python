print("\nExercicio 2")

nome = input("Digite seu nome: ") #Usuário digita o nome
sobrenome = input("Digite seu sobrenome: ") #Usuário digita o sobrenome

nomePrimeiraLetra = nome[0] #A variavel nomePrimeiraLetra recebe a primeira letra da string armazenada na variavel nome
stringEmail = "@algoritimos.com.br"

concatenado = nomePrimeiraLetra + sobrenome + stringEmail #Concatenação das strings

print("Sr(a) {} {}, seu email é {}".format(nome, sobrenome, concatenado)) #Print do resultado
