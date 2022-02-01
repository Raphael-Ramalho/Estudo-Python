from dataclasses import replace
from sys import flags
from numpy import number
import pandas as pd #import da biblioteca pandas e substituição de seu nome por pd
# encoder iso-8859


# nf_2021 = pd.read_csv('D:/Repositorios_github/Estudo-Python/tcc/banco_de _dados/novaFriburgo_2021.csv',sep=';',header=8,encoding='iso8859-15') #essa linha serve para ler o arquivo alvo csv. O primeiro parametro é o caminho do arquivo e o segundo é o separador. O terceiro indica qual é a linha que contém o nome das colunas, enquanto o quarto mostra qual encoding será usado para ler os caracteres do documento. o metodo .read_ pode ser combinado com outros tipos de arquico como json, excel, entre outros. para visualizar os disponíveis, digite .read_ e espere o a IDE sugerir possiveis complementos.

db = pd.read_csv('https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv')


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
# print(nf_2021.iloc[:4]) #do inicio até o 3.

#Acessar linhas e colunas individuais
# print(nf_2021.iloc[2,1]) #linha 2, coluna 1

#Localizar elemento 
# print(nf_2021.loc[nf_2021["PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)"] == '897,6']) #localiza na coluna 'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)', as linhas com o valor '897,6'

#Acessar linhas por nome
#o iterrow() gera uma iteração sobre linhas
# for indice, linha in nf_2021.iterrows() : 
#   linha_ponto = linha['PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)'].replace(',','.') #replace substituindo ',' por '.'
#   print(linha_ponto)
#   if(float(linha_ponto) > 898.2) :
#     break

#Valores estarísticos, como numero de celulas non-NA (count), media (mean), norma (o quao espalhados estão os dados) (std), minimo (min), maximo (max).
# print(nf_2021.describe())

#Ordenação por ordem alfabetica
# nf_2021.sort_values('Nome', ascending) #o ascending pode ser igual a true ou false para indicar se a ordenação é ascendente ou descendente

# MUDANÇA NOS DADOS

# criação de uma nova coluna que possue a soma de outras colunas
# nf_2021['total'] = nf_2021['ataque'] + nf_2021['atq esp'] + nf_2021['def esp'] 

# remoção de coluna
# nf_2021 = nf_2021.drop(columns=['total'])

#renomeação 
# nf_2021.rename({'defensa':'Defesa'}, axis=1)

#reordenar colunas
# cols = list(nf_2021.columns.values)
# nf_2021 = nf_2021

#salvar em csv
# nf_2021.to_csv('modificado.csv')


#filtragem de dados
# novo_db = db.loc[(db['Type 1'] == 'Fire')] # criou uma nova tabela apenas com os pokemons de fogo
# novo_db = db.loc[(db['Type 1'] == 'Fire') & (db['Type 2'] == 'Water')] # criou uma nova tabela apenas com os pokemons de fogo E agua
# novo_db = db.loc[(db['Type 1'] == 'Fire') | (db['Type 2'] == 'Water')] # criou uma nova tabela apenas com os pokemons de fogo OU agua
# novo_db.reset_index(drop=True, inplace=True) # o reset_index reseta o index da tabela, o drop=True deleta o index antigo e o inplace=True fala que o a edição será feita sobre o bando de dados antigo, e n sobre uma cópia dele.
# print(novo_db)

#filtrando versões que possuem mega
# novo_db = db.loc[db['Name'].str.contains('Mega ')] #o metodo .str.contains procura por ocorrências de determinada sub string em uma string maior
# print(novo_db)

# filtrando versões que não possuem mega
# novo_db = db.loc[~db['Name'].str.contains('Mega ')] #o metodo .str.contains procura por ocorrências de determinada sub string em uma string maior
# print(novo_db)

#expressão para pokemons de agua ou fogo
import re #importação de expressão regulares
# novo_db = db.loc[db['Type 1'].str.contains('Fire|Water', flags=re.I, regex=True)] #serve para ignorar upp and lower cases

#pokemons que começam com pi
novo_db = db.loc[db['Name'].str.contains('^pi', flags=re.I, regex=True)] #serve para ignorar upp and lower cases

#mudanças condicionais
# db.loc[db['Type 1'] == 'Fire', 'Type 1'] = 'Fogueteiro'
db.loc[db['HP'] > 500, 'Lendario'] = True
print(db)

