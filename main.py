import sys
import pandas as pd

dataset = pd.read_excel(str(sys.argv[1]) )

estaciones_mas_fallas = dataset[['Id_Avería', 'FECHA', 'Localizacion', 'DESCRIPRD']].groupby(['Localizacion', 'FECHA']).agg(['count']).sort_values(by=['FECHA' ,'Localizacion'], ascending=False)



dia_mas_averias = dataset[['Localizacion', 'FECHA']].groupby(['FECHA'])['FECHA'].count()
dia_mas_averias = dia_mas_averias.to_frame().rename(columns= {'FECHA': 'conteo_averias'})


estaciones_mas_fallas.to_csv('estaciones_mas_fallas.csv')
dia_mas_averias.to_csv('dia_mas_averias.csv')
print("Terminado")
