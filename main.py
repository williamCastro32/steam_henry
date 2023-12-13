from funciones import *
from fastapi import FastAPI
import pandas as pdpip

app = FastAPI(debug=True)

#http://127.0.0.1:8000

@app.get('/')
def bienvenida():
    return {'API de consultas a una base de datos de Steam, /docs en el link para acceder a las funciones de consultas.'}

@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenres(genero:str):
    
    '''Esta función debe devolver año con mas horas jugadas para dicho género.
    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}'''
    
    try:
        return PlayTimeGenre(genero)
    except Exception as e:
        return {"Error":str(e)}
    
@app.get('/UserForGenre/{genero}')
def UserForGenres(genero:str):
    
    '''Esta función devolver el usuario que acumula más horas jugadas para el género dado y una lista
    de la acumulación de horas jugadas por año.Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" :
      us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}'''
    
    try:
        return UserForGenre(genero)
    except Exception as e:
        return {"Error":str(e)}
    
@app.get('/UsersRecommend/{year}')
def UsersRecommends(year:int):
    
    '''Esta función el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = 
    True y comentarios positivos/neutrales) Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]'''
    
    try:
        return UsersRecommend(year)
    except Exception as e:
        return {"Error":str(e)}
    
@app.get('/UsersNotRecommend/{year}')
def UsersNotRecommends(year:int):
    
    '''Esta función el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)    
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]'''
    
    try:
        return UsersNotRecommend(year)
    except Exception as e:
        return {"Error":str(e)}
    
@app.get('/sentimentanalysis/{year}')
def sentiment_analys(year:int):
    '''Esta funcion según el año de lanzamiento, se devuelve una lista con la cantidad de 
    registros de reseñas de usuarios que se encuentren categorizados con un análisis de 
    sentimiento. Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}'''

    try:
        return sentiment_analysis(year)
    except Exception as e:
        return {"Error": str(e)}