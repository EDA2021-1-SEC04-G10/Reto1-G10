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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista para guardar
    todos los videos y crea una lista para guardar las category id
    Retorna el catálogo inicializado
    """
    catalog = {'videos': None,
                'categoryid': None}

    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST',
                                    cmpfunction=cmpVideos)
    catalog['categoryid'] = lt.newList(datastructure='ARRAY_LIST',
                                        cmpfunction=cmpCategoryId)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    """
    Adiciona un video a la lista de videos
    """
    lt.addLast(catalog['videos'], video)

def addCategoryId(catalog, categoryid):
    """
    Adiciona un 'category id' a la lista de category id
    """
    lt.addLast(catalog['categoryid'], categoryid)

# Funciones para creacion de datos

# Funciones de consulta

def getCategoryId(catalog, categoryname):
    """
    Obtiene el 'id' de una categoría por su nombre
    """
    for category in lt.iterator(catalog['categoryid']):
        if categoryname in category['name']:
            return category['id']

def getVideosByCategory(catalog, categoryid):
    """
    Crea la lista de videos de la categoría seleccionada
    """
    videosByCategory = lt.newList(datastructure='ARRAY_LIST',
                                        cmpfunction=cmpVideos)
    for video in lt.iterator(catalog['videos']):
        if categoryid == video['category_id']:
            lt.addLast(videosByCategory, video)
    return videosByCategory

def getVideosByCountry(catalog, country):
    """
    Crea la lista de videos del país seleccionado
    """
    videosByCountry = lt.newList(datastructure='ARRAY_LIST',
                                        cmpfunction=cmpVideos)
    for video in lt.iterator(catalog['videos']):
        if country == video['country']:
            lt.addLast(videosByCountry, video)
    return videosByCountry

def getVideosByCategoryAndCountry(catalog, categoryid, country):
    """
    Crea la lista de videos de la categoría y país seleccionados
    """
    videosByCategoryAndCountry = lt.newList(datastructure='ARRAY_LIST',
                                            cmpfunction=cmpVideos)
    for video in lt.iterator(catalog['videos']):
        if categoryid == video['category_id'] and country == video['country']:
            lt.addLast(videosByCategoryAndCountry, video)
    return videosByCategoryAndCountry

def getFirstVideoByTrendingDays(catalog):
    """
    Obtiene la infomación del video con más 'trending days'
    y su respectivo número de 'trending days'
    """
    size = int(lt.size(catalog))
    videosByTrendingDays = {}
    i = 1
    while i <= size:
        videoId = lt.getElement(catalog, i)['video_id']
        if videoId in videosByTrendingDays:
            videosByTrendingDays[videoId] += 1
        else:
            videosByTrendingDays[videoId] = 1
        i += 1
    videosByTrendingDays.pop('#NAME?', None)
    firstVideoByTrendingDaysKey = max(videosByTrendingDays, 
                                        key=videosByTrendingDays.get)
    firstVideoByTrendingDays = None
    for video in lt.iterator(catalog):
        if video['video_id'] == firstVideoByTrendingDaysKey:
            firstVideoByTrendingDays = video
    trendingDays = videosByTrendingDays[firstVideoByTrendingDaysKey]
    return firstVideoByTrendingDays, trendingDays

def getVideosByCountryAndTag(catalog, country, tag):
    """
    Crea la lista de videos del país y tag seleccionados
    """
    subTag = tag
    videosByCountryAndTag = lt.newList(datastructure='ARRAY_LIST',
                                            cmpfunction=cmpVideos)
    for video in lt.iterator(catalog['videos']):
        if country == video['country'] and subTag in video['tags']:
            lt.addLast(videosByCountryAndTag, video)
    return videosByCountryAndTag
    
# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideos(videotitle, video):
    if (videotitle.lower() in video['title'].lower()):
        return -1
    return 0

def cmpCategoryId(categoryname, category):
    return (categoryname == category['categoryname'])

def cmpVideosByViews(video1, video2):
    """
    Compara dos videos por su número de 'views'
    """
    return (float(video1['views']) > float(video2['views']))

def cmpVideosById(video1, video2):
    """
    Compara dos videos por su 'video_id'
    """
    return (str(video1['video_id']) > str(video2['video_id']))

def cmpVideosByLikes(video1, video2):
    """
    Compara dos videos por su número de 'likes'
    """
    return (float(video1['likes']) > float(video2['likes']))

# Funciones de ordenamiento

def sortVideosByViews(catalog):
    """
    Ordena el catálogo de videos por su número de 'views'
    """
    sortVideosByViews = ms.sort(catalog, cmpVideosByViews)
    return sortVideosByViews

def sortVideosById(catalog):
    """
    Ordena el catálogo de videos por sus 'video_id'
    """
    sortVideosById = ms.sort(catalog, cmpVideosById)
    return sortVideosById

def sortVideosByLikes(catalog):
    """
    Ordena el catálogo de videos por su número de 'likes'
    """
    sortVideosByLikes = ms.sort(catalog, cmpVideosByLikes)
    return sortVideosByLikes