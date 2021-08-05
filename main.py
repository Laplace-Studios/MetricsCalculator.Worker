import sys
import pandas as pd
import plotly.express as px

dataset = pd.read_excel(str(sys.argv[1]) )

estaciones_mas_fallas = dataset[['Id_Avería', 'FECHA', 'Localizacion', 'DESCRIPRD']].groupby(['Localizacion', 'FECHA']).agg(['count']).sort_values(by=['FECHA' ,'Localizacion'], ascending=False)


seccion_mas_averias = dataset[['Seccion1']].groupby(
                                                    ['Seccion1']
                                                    )['Seccion1'].count().to_frame().rename(
                                                        columns= {'Seccion1': 'conteo_averias'}
                                                    ).reset_index().sort_values(by=['conteo_averias' ,'Seccion1'], ascending=False)

seccion_mas_averias_con_retraso = dataset.loc[dataset['Ret_Min'] > 0][['Seccion1']].groupby(
                                                                                            ['Seccion1']
                                                                                            )['Seccion1'].count().to_frame().rename(
                                                        columns= {'Seccion1': 'conteo_averias'}
                                                    ).reset_index().sort_values(by=['conteo_averias' ,'Seccion1'], ascending=False)

print(seccion_mas_averias)


dia_mas_averias = dataset[['Localizacion', 'FECHA']].groupby(['FECHA'])['FECHA'].count()
dia_mas_averias = dia_mas_averias.to_frame().rename(columns= {'FECHA': 'conteo_averias'})


seccion_mas_averias.to_csv('seccion_mas_averias.csv')
seccion_mas_averias_con_retraso.to_csv('seccion_mas_averias_con_retraso.csv')

fig = px.bar(seccion_mas_averias, x='Seccion1', y='conteo_averias')
fig.show()

print("Terminado")
