import pandas as pd
import gzip

'''FUNCION_1'''

def PlayTimeGenre(genero: str):
    '''Esta función debe devolver año con mas horas jugadas para dicho género.
    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}'''
    
    # Leer el DataFrame desde el archivo CSV
    merged_df = pd.read_csv('../datasets/data_funcion1.csv.gz')

    # Capitalizar la primera letra del género
    genero = genero.capitalize()

    # Filtrar el DataFrame para obtener solo las filas relacionadas con el género específico
    filtro_df = merged_df[merged_df['genres'].apply(lambda x: genero in x)]

    if not filtro_df.empty:
        # Agrupar por año sumando las horas jugadas para cada año
        grouped_df = filtro_df.groupby('year')['playtime_forever'].sum().reset_index()

        # Encontrar el año con la mayor cantidad de horas jugadas
        max_year = grouped_df.loc[grouped_df['playtime_forever'].idxmax()]['year']

        return {"Año de lanzamiento con más horas jugadas para Género {}:".format(genero): int(max_year)}
    else:
        return {"Género {} no encontrado en el DataFrame.".format(genero): None}
    
    '''FUNCION_2'''