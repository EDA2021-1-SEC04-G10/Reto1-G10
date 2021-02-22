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
    print("5- Consultar videos con más likes por tag")
    print("0- Salir")

def initCatalog(datastructure):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(datastructure)

def loadData(catalog):
    """
    Carga la información de los videos al catalogo
    """
    controller.loadData(catalog)

def printFirstVideo():
    """
    Imprime la información del primer video de la lista
    """
    print("El primer video cargado es: ")
    print("Título: " + lt.firstElement(catalog['videos'])['title'])
    print("Canal: " + lt.firstElement(catalog['videos'])['channel_title'])
    print("Fecha de tendencia: " + lt.firstElement(catalog['videos'])['trending_date'])
    print("País: " + lt.firstElement(catalog['videos'])['country'])
    print("Views: " + lt.firstElement(catalog['videos'])['views'])
    print("Likes: " + lt.firstElement(catalog['videos'])['likes'])
    print("Dislikes: " + lt.firstElement(catalog['videos'])['dislikes'])

def printCategoryList():
    """
    Imprime la lista de categorías cargadas
    """
    print("Las categorías cargadas son: ")
    for category in lt.iterator(catalog['categoryid']):
        print(category['id\tname'])

def printSortedVideos(sortedvideos, sample=10):
    """
    Imprime la información de los primeros videos ordenados
    """
    size = int(lt.size(sortedvideos))
    if size > sample:
        print("Los primeros " + str(sample) + " videos ordenados son: ")
        i = 1
        while i <= sample:
            video = lt.getElement(sortedvideos, i)
            print("Título: " + video['title'] + "  Views:  " + video['views'])
            i += 1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        datastructure = str(input('Seleccione la estructura de datos\nARRAY_LIST o SINGLE_LINKED\n'))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(datastructure)
        loadData(catalog)
        print("Videos cargados: " + str(lt.size(catalog['videos'])))
        printFirstVideo()
        printCategoryList()

    elif int(inputs[0]) == 2:
        size = int(input('Ingrese el tamaño de la muestra\n'))
        if size > lt.size(catalog['videos']):
            print("El tamaño de muestra excede el tamaño del catálogo")
        else:
            sortingAlgorithm = str(input('Seleccione el algoritmo de ordenamiento\nshell sort, insertion sort o selection sort\n'))
            sortedVideos = controller.sortVideos(catalog, size, sortingAlgorithm)
            print("Para la muestra de " + str(size) + " elementos, el tiempo (mseg) es: " + str(sortedVideos[0]))
            printSortedVideos(sortedVideos[1])

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
