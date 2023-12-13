import pandas as pd


'''FUNCION_1'''

def PlayTimeGenre(genero: str):
    '''Esta función debe devolver año con mas horas jugadas para dicho género.
    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}'''
    
    # Leer el DataFrame desde el archivo CSV
    merged_df = pd.read_csv('./datasets/data_funcion1.csv.gz')

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

def UserForGenre(genero: str):

    '''Esta función devolver el usuario que acumula más horas jugadas para el género dado y una lista
    de la acumulación de horas jugadas por año.Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" :
      us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}'''

    # Leer el DataFrame desde el archivo CSV
    merged_df2 = pd.read_csv('./datasets/data_funcion2.csv.gz')

    genero = genero.capitalize()
    # Paso 1: Filtrar el DataFrame para el género dado
    filtered_df = merged_df2[merged_df2['genres'].apply(lambda x: genero in x)]

    if not filtered_df.empty:
        # Paso 2: Encontrar el usuario con más horas jugadas
        user_with_max_hours = filtered_df.groupby('user_id')['playtime_forever'].sum().idxmax()

        # Paso 3: Crear una lista de acumulación de horas jugadas por año
        grouped_df = filtered_df.groupby(['year', 'user_id'])['playtime_forever'].sum().reset_index()
        hours_accumulation = [{'Año': int(year), 'Horas': int(hours)} for year, hours in grouped_df.groupby('year')['playtime_forever'].max().items()]

        # Paso 4: Retornar el resultado en el formato deseado
        result = {"Usuario con más horas jugadas para Género {}".format(genero): user_with_max_hours,
                  "Horas jugadas": hours_accumulation}
        return result
    else:
        return {"Género {} no encontrado en el DataFrame.".format(genero): None}  
    
'''Funcion 3'''

def UsersRecommend(anio: int):

    '''Esta función el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = 
    True y comentarios positivos/neutrales) Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]'''

    user_reviews = pd.read_csv('./datasets/data_funcion3_4.csv.gz')
   
    # Paso 1: Filtrar el DataFrame para el año dado
    reviews_anio = user_reviews[user_reviews['year'] == anio]
    
    if reviews_anio.empty:
        return {"mensaje": "No hay revisiones para el año proporcionado."}

    # Paso 2: Filtrar para incluir solo revisiones recomendadas y con sentimiento positivo o neutral
    relevant_reviews = reviews_anio[(reviews_anio['recommend'] == True) & (reviews_anio['sentiment_analysis'].isin([1, 2]))]

    if relevant_reviews.empty:
        return {"mensaje": "No hay revisiones recomendadas y con sentimiento positivo o neutral para el año proporcionado."}

    # Paso 3: Contar la cantidad de recomendaciones para cada juego
    game_recommendation_counts = relevant_reviews.groupby('title')['recommend'].count().reset_index()

    # Paso 4: Ordenar los juegos en función de la cantidad de recomendaciones
    top_games = game_recommendation_counts.sort_values(by='recommend', ascending=False)

    # Paso 5: Seleccionar los tres juegos principales
    top_3_games = top_games.head(3)

    # Paso 6: Crear el formato de retorno deseado
    result = [{"Puesto {}: {}".format(i + 1, title)} for i, title in enumerate(top_3_games['title'][:3])]

    return result

'''Funcion 4'''

def UsersNotRecommend(anio: int):

    '''Esta función el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)    
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]'''

    user_reviews = pd.read_csv('./datasets/data_funcion3_4.csv.gz')
   
    # Paso 1: Filtrar el DataFrame para el año dado
    reviews_anio = user_reviews[user_reviews['year'] == anio]
    
    if reviews_anio.empty:
        return {"mensaje": "No hay revisiones para el año proporcionado."}

    # Paso 2: Filtrar para incluir solo revisiones no recomendadas y con sentimiento negativos
    relevant_reviews = reviews_anio[(reviews_anio['recommend'] == False) & (reviews_anio['sentiment_analysis'] == 0)]

    if relevant_reviews.empty:
        return {"mensaje": "No hay revisiones no recomendadas y con sentimiento negativos para el año proporcionado."}

    # Paso 3: Contar la cantidad de recomendaciones negativas para cada juego
    game_recommendation_counts = relevant_reviews.groupby('title')['recommend'].count().reset_index()

    # Paso 4: Ordenar los juegos en función de la cantidad de recomendaciones
    top_games = game_recommendation_counts.sort_values(by='recommend', ascending=False)

    # Paso 5: Seleccionar los tres juegos principales
    top_3_games = top_games.head(3)

    # Paso 6: Crear el formato de retorno deseado
    result = [{"Puesto {}: {}".format(i + 1, title)} for i, title in enumerate(top_3_games['title'][:3])]

    return result

'''Funcion 5'''

def sentiment_analysis(anio: int):
    '''Esta funcion según el año de lanzamiento, se devuelve una lista con la cantidad de 
    registros de reseñas de usuarios que se encuentren categorizados con un análisis de 
    sentimiento.Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}'''

    merge_df5 = pd.read_csv('./datasets/data_funcion5.csv.gz')

    # Filtrar el DataFrame por el año proporcionado
    relevant_reviews = merge_df5[merge_df5['year'] == anio]

    # Contar la cantidad de registros para cada categoría de análisis de sentimiento
    sentiment_counts = relevant_reviews.groupby('sentiment_analysis').size()

     # Convertir los índices a tipos de datos estándar (int)
    sentiment_counts.index = sentiment_counts.index.astype(int)

    # Crear el diccionario de resultados
    result = {
        'Negative': int(sentiment_counts.get(0, 2)),
        'Neutral': int(sentiment_counts.get(1, 2)),
        'Positive': int(sentiment_counts.get(2, 3))
    }
    

    return  result


