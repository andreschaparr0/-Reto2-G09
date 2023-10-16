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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(struc_list,struc_map,load_factor):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(struc_list,struc_map,load_factor)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, memflag):
    """
    Carga los datos
    """
    print('\nCuántos datos desea cargar?')
    print('1: Pocos datos')
    print('2: 5% de los datos')
    print('3: 10% de los datos')
    print('4: 20% de los datos')
    print('5: 30% de los datos')
    print('6: 50% de los datos')
    print('7: 80% de los datos')
    print('8: 100% de los datos')
    llave = True
    while llave == True:
        size = input("Ingrese la opcion que desea:\n")
        size = int(size)
        if size in range(0,9):
            llave = False
            if size == 1:
                size = "small"
            elif size == 2:
                size = "5pct"
            elif size == 3:
                size = "10pct"
            elif size == 4:
                size = "20pct"
            elif size == 5:
                size = "30pct"
            elif size == 6:
                size = "50pct"
            elif size == 7:
                size = "80pct"
            elif size == 8:
                size = "large"
            if memflag:
                match_results, goal_scorers, shootouts, delta_time_value, delta_memory_value = controller.load_data(control, size, memflag)
            else:
                match_results, goal_scorers, shootouts, delta_time_value = controller.load_data(control, size, memflag)
        else:
            print("ingrese una opción valida")
    print("Ahora ingrese el metodo con el cual desea ordenar los datos:")
    print('Opción 1: Selection sort')
    print('Opción 2: Insertion sort')
    print('Opción 3: Shell sort')
    print('Opcion 4: Quick sort')
    print('Opcion 5: Merge sort\n')
    metodo = input()
    metodo = int(metodo)
    controller.sort(control, metodo)
    print_tabulated_data(control)
    print(control["model"]["scorer"])
    if memflag:
        return match_results, goal_scorers, shootouts, delta_time_value, delta_memory_value 
    else:
        return match_results, goal_scorers, shootouts, delta_time_value

def print_tabulated_data(control):
    headers1=["Fecha",
             "local",
             "visitante",
             "puntuacion local",
             "puntuacion visitante",
             "Torneo",
             "Ciudad",
             "Pais"]
    headers2=["Fecha",
             "local",
             "visitante",
             "equipo",
             "anotador",
             "minuto"]
    headers3=["Fecha",
             "local",
             "visitante",
             "ganador"]
    datos = controller.get_firts_and_last_3(control["model"],"match_results")
    print(tabulate(datos, headers= headers1, tablefmt="grid"))
    datos = controller.get_firts_and_last_3(control["model"],'goal_scorers')
    print(tabulate(datos, headers= headers2, tablefmt="grid"))
    datos = controller.get_firts_and_last_3(control["model"],'shootouts')
    print(tabulate(datos, headers= headers3, tablefmt="grid"))  
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    
    pass
def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', 1, True):
        return True
    else:
        return False
    
# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                tipo_list = input("Ingrese que tipo de lista quiere utilizar. \n1 Para ARRAY LIST\n2 Para SINGLE LINKED\n")
                tipo_map = input("\nIngrese que mecanismo de colisiones quiere utilizar. \n1 Para CHAINING \n2 Para PROBING\n")
                if tipo_list in ["1","2"]:
                    if tipo_list == "1":
                        struc_list = 'ARRAY_LIST'
                    elif tipo_list == "2":
                        struc_list = 'SINGLE_LINKED'
                if tipo_map in ["1","2"]:
                    if tipo_map == "1":
                        struc_map = "CHAINING"
                    elif tipo_map == "2":
                        struc_map = 'PROBING'
                    load_factor=float(input("Seleccione el factor de carga que desea utilizar: "))
                    control = new_controller(struc_list,struc_map,load_factor)
                    memflag=castBoolean(input("Desea medir la memoria utilizada? (True/False): "))
                    print("Cargando información de los archivos ....\n")
                    partidos = load_data(control, memflag)                    
                    print('Partidos cargados: ' + str(partidos[0]) + ' goles cargados: '+ str(partidos[1]) + " shootous cargados: " + str(partidos[2]))
                    print('El tiempo de carga es de '+ str(round(partidos[3],2)) + ' segundos')
                    if memflag:
                        print('El espacio usado de carga es de '+ str(round(partidos[4],2)) + 'KB')
                else:
                    print("Ingrese una opcion valida")            
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa") 
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese un opción valida.\n")
    sys.exit(0)
