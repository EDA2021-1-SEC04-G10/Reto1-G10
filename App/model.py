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
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import selectionsort as se
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(datastructure):
    """
    Inicializa el catalogo de videos. Crea una lista para guardar
    todos los videos y crea una lista para guardar las category id
    Retorna el catalogo inicializado
    """
    catalog = {'videos': None,
                'categoryid': None}

    catalog['videos'] = lt.newList(datastructure=datastructure,
                                    cmpfunction=cmpVideos)
    catalog['categoryid'] = lt.newList(datastructure=datastructure,
                                        cmpfunction=cmpCategoryId)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    """
    Adicionar un video a la lista de videos
    """
    lt.addLast(catalog['videos'], video)

def addCategoryId(catalog, categoryid):
    """
    Adicionar un category id a la lista de category id
    """
    lt.addLast(catalog['categoryid'], categoryid)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideos(videotitle, video):
    if (videotitle.lower() in video['title'].lower()):
        return -1
    return 0

def cmpCategoryId(categoryname, category):
    return (categoryname == category['categoryname'])

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero si los 'views' del video1 son menores que los 'views'
    del video2

    Args:
        video1: información del primer video que incluye su valor de 'views'
        video2: información del segundo video que incluye su valor de 'views'
    """
    return (float(video1['views']) > float(video2['views']))

# Funciones de ordenamiento

def sortVideos(catalog, size, sortingalgorithm):
    """
    Crea una sublista ordenada de acuerdo al algoritmo de ordenamiento
    seleccionado

    Args:
        catalog: catálogo en el que se alamcenan los videos
        size: tamaño seleccionado de la sublista 
        sortingalgoritm: algoritmo de ordernamiento seleccionado
    
    Returns:
        La sublista ordenada de videos
    """
    subList = lt.subList(catalog['videos'], 1, size)
    subList = subList.copy()
    startTime = time.process_time()

    if sortingalgorithm == 'shell sort':
        sortedList = sa.sort(subList, cmpVideosByViews)
    elif sortingalgorithm == 'insertion sort':
        sortedList = si.sort(subList, cmpVideosByViews)
    elif sortingalgorithm == 'selection sort':
        sortedList = se.sort(subList, cmpVideosByViews)

    stopTime = time.process_time()
    elapsepTimeMseg = (stopTime - startTime)*1000

    return elapsepTimeMseg, sortedList