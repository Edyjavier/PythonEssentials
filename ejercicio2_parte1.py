# -*- coding: utf-8 -*-
"""
Ejercicios de Python

Created on Mon May 23 09:38:53 2022

@author: Edison Tamayo
"""
"""
Parte 1
Considerando la siguiente tupla codifique un programa que permita separar los números pares 
e impares. Identifique también los posibles valores que considere atípicos a ese arreglo.
Datos_2021 = [1, 2, 3, ,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]"""
Datos_2021 = [1, 2, 3,'',4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]
lista=list(Datos_2021)
list_num_pares=[]
list_num_impares=[]
list_atipicos=[]
for elemento in lista:
    if type(elemento) == int:
        if (elemento%2):
            list_num_impares.append(elemento)
        else:
            list_num_pares.append(elemento)
    else:
        list_atipicos.append(elemento)
print("Números pares: ",list_num_pares)
print("Números impares: ",list_num_impares)
print("Valores atípicos: ",list_atipicos)
    

