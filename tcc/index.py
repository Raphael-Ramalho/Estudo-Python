import pandas as pd #import da biblioteca pandas e substituição de seu nome por pd
# encoder iso-8859


nf_2021 = pd.read_csv('D:/Repositorios_github/Estudo-Python/tcc/banco_de _dados/novaFriburgo_2021.csv',sep=';',header=8,encoding='iso8859-15') #essa linha serve para ler o arquivo alvo csv. O primeiro parametro é o caminho do arquivo e o segundo é o separador. O terceiro indica qual é a linha que contém o nome das colunas, enquanto o quarto mostra qual encoding será usado para ler os caracteres do documento. o metodo .read_ pode ser combinado com outros tipos de arquico como json, excel, entre outros. para visualizar os disponíveis, digite .read_ e espere o a IDE sugerir possiveis complementos.


# print(nf_2021.columns) # exibe as colunas
# print(nf_2021.head(9)) # faz o python exibir as 9 primeiras linhas da tabela
# print(nf_2021.tail(9)) # faz o python exibir as 9 ultimas linhas da tabela


# Acessar apenas uma coluna
# print(nf_2021["PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)"])

#Acessar duas ou mais colunas
# print(nf_2021[["PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)", 'PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)']])
#da linha 5 até a 9
# print(nf_2021[["PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)", 'PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)']][5:10])
#da linha 5 até a 19, de 2 em 2
# print(nf_2021[["PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)", 'PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)']][5:21:2])

#Acessar linhas 
# print(nf_2021.iloc[:4]) #do inicio até a 4

#Acessar linhas e colunas individuais
# print(nf_2021.iloc[2,1]) #linha 2, coluna 1

#Localizar elemento 
# print(nf_2021.loc[nf_2021["PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)"] == '897,6']) #localiza na coluna 'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)', as linhas com o valor '897,6'

#Acessar linhas por nome
for indice, linha in nf_2021.iterrows()

