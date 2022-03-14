import pandas as pd
import matplotlib.pyplot as plt

#Leitura do arquivo
notas = pd.read_csv("dados/ratings.csv")

#Muda os nomes da coluna
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]

notas.nota.plot(kind='hist')
