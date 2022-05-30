# -*- coding: utf-8 -*-
"""
Ejercicios de Python

Created on Sat May 21 14:01:20 2022

@author: Edison Tamayo
"""
def ejercicios1():
    print("Empezando a trabajar con Python")
    print("Realizado por: \"Edison Tamayo\"")
    print("Consultando los tipos de valores:")
    """En este ejercicio utilizamos la función type, obteniendo un resultado entero"""
    print("El tipo de dato de 875 es: ",type(875))
    """En este ejercicio utilizamos la función type, obteniendo un resultado float"""
    print("El tipo de dato de 4.89 es: ",type(4.89))
    """En este ejercicio utilizamos la función type, obteniendo un resultado string"""
    print("El tipo de dato del texto: Now is better than never. es:",type("Now is better than never."))
    """En este ejercicio utilizamos la función type, obteniendo un resultado float"""
    print("El tipo de dato de 1.32 es: ",type(1.32))
    """En este ejercicio identificamos que 5 + 8i no se pueden sumar, porque es un string ya que 8i 
    no se considera número imaginario en Python, debería ser 8j, por lo tanto NO es entero"""
    print("¿El valor 5 + 8i corresponde a un valor entero? NO es entero, ni imaginario sino es un texto")
    """"Utilizo la función int para verificar si es entero o no"""
    print("¿El valor 8.2 corresponde a un valor entero?")
    if int(8.2): 
        print("SI") 
    else: 
        print("NO")
    """"Utilizo la función str para verificar si es un string"""
    print("¿El texto: Readability counts. corresponde a un string?")
    if str("Readability counts."): 
        print("SI") 
    else: 
        print("NO")
    return
