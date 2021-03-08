"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf

sys.setrecursionlimit(1000*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información de videos en el catálogo")
    print("2- Consultar videos tendencia con más views por categoría y país")
    print("3- Consultar video tendencia por país")
    print("4- Consultar video tendencia por categoría")
    print("5- Consultar videos con más likes por país y tag")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catálogo de videos
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga la información de los videos al catálogo
    """
    controller.loadData(catalog)

def printFirstVideo(catalog):
    """
    Imprime la información del primer video de la lista
    """
    firstVideo = lt.firstElement(catalog['videos'])
    print("El primer video cargado es: ")
    print("Título: " + firstVideo['title'] + "  Canal: " + firstVideo['channel_title'] +
    "  Fecha de tendencia: " + firstVideo['trending_date'] + "  País: " + firstVideo['country'] +
    "  Views: " + firstVideo['views'] + "  Likes: " + firstVideo['likes'] + "  Dislikes: " + firstVideo['dislikes'])

def printCategoryList(catalog):
    """
    Imprime la lista de categorías cargadas
    """
    print("Las categorías cargadas son: ")
    for category in lt.iterator(catalog['categoryid']):
        print(category['id'] + category['name'])

def printSortedVideosByViews(sortedvideos, sample, categoryname, country):
    """
    Imprime la información de los videos con más 'views' de un país
    y categoría específica
    """
    size = int(lt.size(sortedvideos))
    if size > sample:
        print("Los " + str(sample) + " videos con más views de la categoría " + str(categoryname) +
        " de " + str(country) + " son: ")
        i = 1
        while i <= sample:
            video = lt.getElement(sortedvideos, i)
            print("Fecha de tendencia: " + video['trending_date'] + "  Título: " + video['title'] + 
            "  Canal: " + video['channel_title'] + "  Fecha de publicación: " + video['publish_time'] +
            "  Views: " + video['views'] + "  Likes: " + video['likes'] + "  Dislikes: " + video['dislikes'])
            i += 1

def printSortedVideosByLikes(sortedvideos, sample, country, tag):
    """
    Imprime la información de los videos con más 'likes' de un país
    con un tag específico
    """
    size = int(lt.size(sortedvideos))
    if size > sample:
        print("Los " + str(sample) + " videos con más likes del país " + str(country) +
        " con el tag " + str(tag) + " son: ")
        i = 1
        while i <= sample:
            video = lt.getElement(sortedvideos, i)
            print("Título: " + video['title'] + "  Canal: " + video['channel_title'] + "  Fecha de publicación: " +
            video['publish_time'] + "  Views: " + video['views'] + "  Likes: " + video['likes'] + "  Dislikes:  " +
            video['dislikes'] + "  Tags: " + video['tags'])
            i += 1

def printFirstVideoByTrendingDaysByCountry(firstVideoByTrendingDays, country):
    """
    Imprime la información del video con más 'trending days' de un país
    específico
    """
    video = firstVideoByTrendingDays[0]
    trendingDays = firstVideoByTrendingDays[1]
    print("El video con más trending days del país " + str(country) +
    " es: ")
    print("Título: " + video['title'] + "  Canal: " + video['channel_title'] + "  País: " + video['country'] +
    "  Días de tendencia: " + str(trendingDays))

def printFirstVideoByTrendingDaysByCategory(firstVideoByTrendingDays, categoryid, categoryname):
    """
    Imprime la información del video con más 'trending days' de una
    categoría específica
    """
    video = firstVideoByTrendingDays[0]
    trendingDays = firstVideoByTrendingDays[1]
    print("El video con más trending days de la categoría " + str(categoryname) +
    " es: ")
    print("Título: " + video['title'] + "  Canal: " + video['channel_title'] + "  Categoría: " + str(categoryid) +
    "  Días de tendencia: " + str(trendingDays))

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input("Seleccione una opción para continuar\n")
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print("El número de videos cargados es: " + str(lt.size(catalog['videos'])))
        printFirstVideo(catalog)
        printCategoryList(catalog)

    elif int(inputs[0]) == 2:
        categoryname = str(input("Ingrese la categoría\n"))
        categoryid = controller.getCategoryId(catalog, categoryname)
        country = str(input("Ingrese el país\n"))
        size = int(input("Ingrese el número de videos a listar\n"))
        videos = controller.getVideosByCategoryAndCountry(catalog, categoryid, country)
        sortedVideos = controller.sortVideosByViews(videos)
        if size > lt.size(videos):
            print("El número de videos excede el tamaño del catálogo\n")
        else:
            printSortedVideosByViews(sortedVideos, size, categoryname, country)

    elif int(inputs[0]) == 3:
        country = str(input("Ingrese el país\n"))
        videos = controller.getVideosByCountry(catalog, country)
        sortedVideos = controller.sortVideosById(videos)
        firstVideoByTrendingDays = controller.getFirstVideoByTrendingDays(sortedVideos)
        printFirstVideoByTrendingDaysByCountry(firstVideoByTrendingDays, country)

    elif int(inputs[0]) == 4:
        categoryname = str(input("Ingrese la categoría\n"))
        categoryid = controller.getCategoryId(catalog, categoryname)
        videos = controller.getVideosByCategory(catalog, categoryid)
        sortedVideos = controller.sortVideosById(videos)
        firstVideoByTrendingDays = controller.getFirstVideoByTrendingDays(sortedVideos)
        printFirstVideoByTrendingDaysByCategory(firstVideoByTrendingDays, categoryid, categoryname)

    elif int(inputs[0]) == 5:
        country = str(input("Ingrese el país\n"))
        tag = str(input("Ingrese el tag\n"))
        size = int(input("Ingrese el número de videos a listar\n"))
        videos = controller.getVideosByCountryAndTag(catalog, country, tag)
        sortedVideos = controller.sortVideosByLikes(videos)
        if size > lt.size(videos):
            print("El número de videos excede el tamaño del catálogo\n")
        else:
            printSortedVideosByLikes(sortedVideos, size, country, tag)

    else:
        sys.exit(0)
sys.exit(0)
