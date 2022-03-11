import pandas as pd

#Leitura do arquivo
notas = pd.read_csv("dados/ratings.csv")

#Muda os nomes da coluna
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]

print(notas['nota'])
print("="*60)
print(notas['nota'].unique())