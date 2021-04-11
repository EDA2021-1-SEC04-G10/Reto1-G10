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

import time
import tracemalloc
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
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    loadVideos(catalog)
    loadCategoryId(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return deltatime, deltamemory

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
    Carga las categorías del archivo
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
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()
    
    sortedvideos = model.sortVideosByViews(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return sortedvideos, deltatime, deltamemory

def sortVideosById(catalog):
    """
    Ordena los videos por 'video_id'
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    sortedvideos = model.sortVideosById(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return sortedvideos, deltatime, deltamemory

def sortVideosByLikes(catalog):
    """
    Ordena los videos por 'likes'
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    sortedvideos = model.sortVideosByLikes(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return sortedvideos, deltatime, deltamemory

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
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getVideosByCategory(catalog, categoryid)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

def getVideosByCountry(catalog, country):
    """
    Retorna los videos del país seleccionado
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getVideosByCountry(catalog, country)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

def getVideosByCategoryAndCountry(catalog, categoryid, country):
    """
    Retorna los videos de la categoría y país seleccionados
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getVideosByCategoryAndCountry(catalog, categoryid, country)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

def getVideosByCountryAndTag(catalog, country, tag):
    """
    Retorna los videos del país y tag seleccionados
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getVideosByCountryAndTag(catalog, country, tag)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

def getFirstVideoByTrendingDays(catalog):
    """
    Retorna la información del video con más 'trending days'
    """
    deltatime = -1.0
    deltamemory = -1.0

    tracemalloc.start()
    starttime = getTime()
    startmemory = getMemory()

    videos = model.getFirstVideoByTrendingDays(catalog)

    stopmemory = getMemory()
    stoptime = getTime()
    tracemalloc.stop()

    deltatime = stoptime - starttime
    deltamemory = deltaMemory(startmemory, stopmemory)
    return videos, deltatime, deltamemory

# Funciones para medir tiempo y memoria

def getTime():
    """
    Retorna el instante de tiempo de procesamiento en
    milisegundos
    """
    return float(time.perf_counter()*1000)

def getMemory():
    """
    Retorna la memoria alocada en un instante de tiempo
    """
    return tracemalloc.take_snapshot()

def deltaMemory(startmemory, stopmemory):
    """
    Retorna la diferencia de memoria alocada entre dos instantes
    de tiempo en bytes
    """
    memorydiff = stopmemory.compare_to(startmemory, 'filename')
    deltamemory = 0.0
    for stat in memorydiff:
        deltamemory = deltamemory + stat.size_diff
    deltamemory = deltamemory/1024.0
    return deltamemory
