import pandas as pd

#Crie um dicionario com os dados de alunos
dados = {
    "nome" : ["Ana", "Bruno", "Carlos", "Diana"],
    "idade" : [20, 22, 19, 21],
    "nota" : [8.5, 7.0, 9.0, 8.0]
}

#Crie dataframe
df = pd.DataFrame(dados)
print(df)

#Calcule estatisticas
print ("\n Estatisticas da Nota:")
print (df["nota"].describe())