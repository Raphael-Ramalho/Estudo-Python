import pandas as pd #import da biblioteca pandas e substituição de seu nome por pd
# encoder iso-8859


nf_2021 = pd.read_csv('D:/Repositorios_github/Estudo-Python/tcc/banco_de _dados/novaFriburgo_2021.csv',sep=';',header=8,encoding='iso8859-1') #essa linha serve para ler o arquivo alvo csv

# nf_2021.head()
print(nf_2021.columns)