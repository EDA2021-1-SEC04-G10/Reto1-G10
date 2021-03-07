"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la función de inicialización del catalogo al modelo
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos en los archivos y carga los datos en las estructuras
    """
    loadVideos(catalog)
    loadCategoryId(catalog)

def loadVideos(catalog):
    """
    Carga los videos del archivo
    """
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategoryId(catalog):
    """
    Carga las categorias del archivo
    """
    categoryidfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryidfile, encoding='utf-8'), delimiter='\t')
    for categoryid in input_file:
        model.addCategoryId(catalog, categoryid)

# Funciones de ordenamiento

def sortVideosByViews(catalog):
    """
    Ordena los videos por 'views'
    """
    return model.sortVideosByViews(catalog)

def sortVideosById(catalog):
    """
    Ordena los videos por 'video_id'
    """
    return model.sortVideosById(catalog)

def sortVideosByLikes(catalog):
    """
    Ordena los videos por 'likes'
    """
    return model.sortVideosByLikes(catalog)

# Funciones de consulta sobre el catálogo

def getCategoryId(catalog, categoryname):
    """
    Retorna el 'id' de una categoría por su nombre
    """
    return model.getCategoryId(catalog, categoryname)

def getVideosByCategory(catalog, categoryid):
    """
    Retorna los videos de la categoría seleccionada
    """
    return model.getVideosByCategory(catalog, categoryid)

def getVideosByCountry(catalog, country):
    """
    Retorna los videos del país seleccionado
    """
    return model.getVideosByCountry(catalog, country)

def getVideosByCategoryAndCountry(catalog, categoryid, country):
    """
    Retorna los videos de la categoría y país seleccionados
    """
    return model.getVideosByCategoryAndCountry(catalog, categoryid, country)

def getVideosByCountryAndTag(catalog, country, tag):
    """
    Retorna los videos del país y tag seleccionados
    """
    return model.getVideosByCountryAndTag(catalog, country, tag)

def getFirstVideoByTrendingDays(catalog):
    """
    Retorna la información del video con más 'trending days'
    """
    return model.getFirstVideoByTrendingDays(catalog)
