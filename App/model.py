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
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(struc_list, struc_map, load_factor):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    football_data = {'match_results': None,
               'goal_scorers': None,
               'shootouts': None,
               'scorer': None}

    football_data['match_results'] = lt.newList(datastructure=struc_list,
                                                cmpfunction=cmp_partidos_by_fecha_y_pais) 
    football_data['goal_scorers'] = lt.newList(datastructure=struc_list,
                                               cmpfunction=cmp_partidos_by_fecha_y_pais) 
    football_data['shootouts'] = lt.newList(datastructure=struc_list,
                                            cmpfunction=cmp_partidos_by_fecha_y_pais)
    football_data['scorer'] = mp.newMap(152,
                             maptype=struc_map,
                             loadfactor=load_factor)
    return football_data


# Funciones para agregar informacion al modelo

def add_result(football_data, data, tipo):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    nuevo2 = new_result(data,tipo)
    lt.addLast(football_data[tipo], nuevo2)


# Funciones para creacion de datos

def new_result(data, tipo):
    """
    Crea una nueva estructura para modelar los datos
    """
    nuevo = None
    if tipo == "match_results":
        nuevo = {"fecha":data["date"],"local": data["home_team"],"visitante": data["away_team"],"puntuacion local": data["home_score"],"puntuacion visitante": data["away_score"],"Torneo": data["tournament"],"Ciudad": data["city"],"Pais": data["country"]}
    elif tipo == "goal_scorers":
        nuevo = {"fecha":data["date"], "local":data["home_team"], "visitante":data["away_team"],"equipo": data["team"], "anotador": data["scorer"], "minuto": data["minute"],"AutoGol": data["own_goal"], "Penalty": data["penalty"] }
    elif tipo == "shootouts":
        nuevo = {"fecha":data["date"],"local": data["home_team"],"visitante": data["away_team"],"ganador": data["winner"]}
    return nuevo

def add_Scorer(football_data, GoalScorer, pubyear):
    years = football_data['scorer']
    pubyear = int(float(pubyear))
    try:
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            año = me.getValue(entry)
        else:
            año = newYear(pubyear)
            mp.put(years, pubyear, año)
        lt.addLast(año['scorers'], GoalScorer)
    except Exception:
        return None

def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "scorers": None}
    entry['year'] = pubyear
    entry['scorers'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(football_data):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(football_data)

def get_firts_and_last_3(model, type):
    primeros = lt.subList(model[type],1, 3)
    ultimos = lt.subList(model[type],lt.size(model[type])-2,3)
    datos = (ultimos,primeros)
    results = [None, None, None, None, None, None]
    for i in range(1,4):
                results[3-i] = get_datos(datos[0],i)
                results[6-i] = get_datos(datos[1],i)
    return results  

def get_datos(datos, pos):
    valores_lista = [valor for valor in lt.getElement(datos,pos).values()]
    return valores_lista

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def cmp_partidos_by_fecha_y_pais(resultado1, resultado2):
    if resultado1["fecha"] < resultado2["fecha"]:
        return 1
    elif resultado1["fecha"] == resultado2["fecha"]:
        if resultado1["local"][0] < resultado2["local"][0]:
            return 1
        else:
            return -1 
    else: 
        return -1
    
def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return -1

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    if data_1["fecha"] < data_2["fecha"]:
        return True
    elif data_1["fecha"] == data_2["fecha"]:
        if data_1["local"][0] < data_2["local"][0]:
            return True
        else:
            return False
    else: 
        return False


def sort(data_structs, metodo):
    """
    Función encargada de ordenar la lista con los datos
    """
    sub_list1 = lt.subList(data_structs["match_results"],1,lt.size(data_structs["match_results"]))
    sub_list2 = lt.subList(data_structs["goal_scorers"],1,lt.size(data_structs["goal_scorers"]))
    sub_list3 = lt.subList(data_structs["shootouts"],1,lt.size(data_structs["shootouts"]))
    if metodo == 1:
        se.sort(sub_list1, sort_criteria)
        se.sort(sub_list2, sort_criteria)
        se.sort(sub_list3, sort_criteria)
    elif metodo == 2:
        ins.sort(sub_list1, sort_criteria)
        ins.sort(sub_list2, sort_criteria)
        ins.sort(sub_list3, sort_criteria)
    elif metodo == 3:
        sa.sort(sub_list1, sort_criteria)
        sa.sort(sub_list2, sort_criteria)
        sa.sort(sub_list3, sort_criteria)
    elif metodo == 4:
        quk.sort(sub_list1, sort_criteria)
        quk.sort(sub_list2, sort_criteria)
        quk.sort(sub_list3, sort_criteria)
    elif metodo == 5:
        merg.sort(sub_list1, sort_criteria)
        merg.sort(sub_list2, sort_criteria)
        merg.sort(sub_list3, sort_criteria)
    data_structs["match_results"] = sub_list1
    data_structs["goal_scorers"] = sub_list2
    data_structs["shootouts"] = sub_list3
