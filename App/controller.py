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
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(struc_list,struc_map,load_factor):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(struc_list,struc_map,load_factor)
    return control


# Funciones para la carga de datos

def load_data(control, size, memflag):
    """
    Carga los datos del reto
    """
    football_data = control["model"]
    match_results = loadResults(football_data, size)
    shootouts = loadShootouts(football_data, size)
    goal_scorers = loadGoalScorers(football_data, size)
    #Medicion inicial de tiempo y memoria
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    #ejecucion principal
    loadScorers(football_data, size)
    #Medicion final de tiempo y memoria
    stop_time = get_time()
    delta_time_value = delta_time(start_time,stop_time)
    
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory_value = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return match_results, goal_scorers, shootouts, delta_time_value, delta_memory_value
    else:
        # respuesta sin medir memoria
        return match_results, goal_scorers, shootouts, delta_time_value

def loadResults(football_data, size):
    texto = "football/results-utf8-" +str(size)+".csv"
    footballfile = cf.data_dir + texto
    input_file = csv.DictReader(open(footballfile, encoding='utf-8'))
    for result in input_file:
        model.add_result(football_data, result, "match_results")
    return model.data_size(football_data["match_results"])

def loadGoalScorers(football_data, size):
    texto = "football/goalscorers-utf8-" +str(size)+".csv"
    footballfile = cf.data_dir +texto
    input_file = csv.DictReader(open(footballfile, encoding='utf-8'))
    for GoalScorer in input_file:
        model.add_result(football_data, GoalScorer, "goal_scorers")
    return model.data_size(football_data["goal_scorers"])

def loadShootouts(football_data, size):
    texto = "football/shootouts-utf8-" +str(size)+".csv"
    footballfile = cf.data_dir + texto
    input_file = csv.DictReader(open(footballfile, encoding='utf-8'))
    for Shootout in input_file:
        model.add_result(football_data, Shootout,"shootouts")
    return model.data_size(football_data["shootouts"])

def loadScorers(football_data, size):
    texto = "football/goalscorers-utf8-" +str(size)+".csv"
    footballfile = cf.data_dir +texto
    input_file = csv.DictReader(open(footballfile, encoding='utf-8'))
    for GoalScorer in input_file:
        año = GoalScorer["date"]
        año = año[:4]
        GoalScorer = GoalScorer["scorer"]
        model.add_Scorer(football_data, GoalScorer, año)
    

# Funciones de ordenamiento

def sort(control, metodo):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    model.sort(control["model"], metodo)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def get_firts_and_last_3(control, type):
    datos = model.get_firts_and_last_3(control,type)
    return datos

def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
