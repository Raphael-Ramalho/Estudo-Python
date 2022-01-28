import pandas as pd #import da biblioteca pandas e substituição de seu nome por pd
# encoder iso-8859


nf_2021 = pd.read_csv('D:/Repositorios_github/Estudo-Python/tcc/banco_de _dados/novaFriburgo_2021.csv',sep=';',header=8,encoding='iso8859-15') #essa linha serve para ler o arquivo alvo csv. O primeiro parametro é o caminho do arquivo e o segundo é o separador. O terceiro indica qual é a linha que contém o nome das colunas, enquanto o quarto mostra qual encoding será usado para ler os caracteres do documento. o metodo .read_ pode ser combinado com outros tipos de arquico como json, excel, entre outros. para visualizar os disponíveis, digite .read_ e espere o a IDE sugerir possiveis complementos.

# print(nf_2021.columns) # exibe as colunas
# print(nf_2021.head(9)) # faz o python exibir as 9 primeiras linhas da tabela
# print(nf_2021.tail(9)) # faz o python exibir as 9 ultimas linhas da tabela

# Acessar apenas uma coluna
nf_2021["PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)"]