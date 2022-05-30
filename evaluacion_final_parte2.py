# -*- coding: utf-8 -*-
"""
Ejercicios de Python

Created on Mon May 28 14:23:34 2022

@author: Edison Tamayo
"""
menu="\nLista de programas realizados en el curso de Python:\n1) Ejercicios 1 Parte 1.\n2) Ejercicios 1 Parte 2.\n3) Ejercicios 2 Parte 1.\n4) Ejercicios 2 Parte 2.\n5) Ejercicios 3.\n6)Salir.\n\nElija una opcion:"

continuar=True
while continuar:
    opcion=input(menu)
    try:
        opcion=int(opcion)
        if opcion==1:
            from modulo_ejercicios1 import *
            ejercicios1()
        elif opcion==2:
           from modulo_ejercicios1_parte2 import *
           ejercicios1_parte2()
        elif opcion==3:
           from modulo_ejercicio2_parte1 import *
           ejercicio2_parte1()
        elif opcion==4:
           from modulo_ejercicio2_parte2 import *
           ejercicio2_parte2()
        elif opcion==5:
           from modulo_ejercicios3 import *
           principal()
        elif opcion==6:
            continuar=False
            print("Gracias por usar este programa de Python!")
            break
        else:
            print("Error, opciones válidas del 1 al 6")
    except ValueError:
        print("Error de excepciones")  

