# Análisis de complejidad :hammer_and_wrench:

## Autores :writing_hand:
* Hernán Buitrago - Req :two:
  * hf.buitrago10@uniandes.edu.co
  * 201512807
* Daniel Aguilera - Req :three:
  * d.aguilera@uniandes.edu.co
  * 202010592

## Requerimientos :white_check_mark:

__Requerimiento 1__ 

* La complejidad del requerimiento es O(n log n).

| Función | Complejidad | Descripción |
| --- | --- | --- |
| ```getCategoryId()``` | O(n) | La función recorre la lista de categorías del catálogo en busca del 'id' para el 'name' de la categoría ingresada por parámetro. |
| ```getVideosByCategoryAndCountry()``` | O(n) | La función crea un ```ARRAY_LIST```; luego recorre la lista de videos del catálogo en busca de los videos con 'category_id' y 'country' ingresados por parámetro y agrega dichos videos al ```ARRAY_LIST``` creado inicialmente. | 
| ```sortVideosByViews()``` | O(n log n) | La función ordena el catálogo de videos por su número de 'views' usando el algoritmo de ordenamiento ```mergesort```. |

__Requerimiento 2__

* La complejidad del requerimiento es O(n log n).

| Función | Complejidad | Descripción |
| --- | --- | --- |
| ```getVideosByCountry()``` | O(n) | La función crea un ```ARRAY_LIST```; luego recorre la lista de videos del catálogo en busca de los videos con 'country' ingresado por parámetro y agrega dichos videos al ```ARRAY_LIST``` creado inicialmente. |
| ```sortVideosbyId()``` | O(n log n) | La función ordena el catálogo de videos por su 'video_id' usando el algoritmo de ordenamiento ```mergesort```. | 
| ```getFirstVideoByTrendingDays()``` | O(n) | La función crea un diccionario, luego obtiene el 'video_id' de cada video de la lista de videos del catálogo y lo agrega al diccionario. Si el 'video_id' no está en el diccionario, crea una nueva llave; si ya está en el diccionario, suma 1 al valor de la llave. Posteriormente, se recorre la lista del catálogo de videos para recuperar la información del video con mayor número de repeticiones a partir de su 'video_id. |

__Requerimiento 3__

* La complejidad del requerimiento es O(n log n).

| Función | Complejidad | Descripción |
| --- | --- | --- |
| ```getCategoryId()``` | O(n) | La función recorre la lista de categorías del catálogo en busca del 'id' para el 'name' de la categoría ingresada por parámetro. |
| ```getVideosByCategory()``` | O(n) | La función crea un ```ARRAY_LIST```; luego recorre la lista de videos del catálogo en busca de los videos con 'category_id' ingresada por parámetro y agrega dichos videos al ```ARRAY_LIST``` creado inicialmente. |
| ```sortVideosbyId()``` | O(n log n) | La función ordena el catálogo de videos por su 'video_id' usando el algoritmo de ordenamiento ```mergesort```. | 
| ```getFirstVideoByTrendingDays()``` | O(n) | La función crea un diccionario, luego obtiene el 'video_id' de cada video de la lista de videos del catálogo y lo agrega al diccionario. Si el 'video_id' no está en el diccionario, crea una nueva llave; si ya está en el diccionario, suma 1 al valor de la llave. Posteriormente, se recorre la lista del catálogo de videos para recuperar la información del video con mayor número de repeticiones a partir de su 'video_id. |

__Requerimiento 4__

* La complejidad del requerimiento es O(n log n).

| Función | Complejidad | Descripción |
| --- | --- | --- |
| ```getVideosByCountryAndTag()``` | O(n) | La función crea un ```ARRAY_LIST```; luego recorre la lista de videos del catálogo en busca de los videos con 'country' y 'tag' ingresados por parámetro y agrega dichos videos al ```ARRAY_LIST``` creado inicialmente. |
| ```sortVideosByLikes()``` | O(n log n) | La función ordena el catálogo de videos por su número de 'likes' usando el algoritmo de ordenamiento ```mergesort```. |
