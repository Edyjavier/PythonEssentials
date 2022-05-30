# -*- coding: utf-8 -*-
"""
Ejercicios de Python

Created on Mon May 23 18:13:58 2022

@author: Edison Tamayo
"""
menu="\nElija una opcion:\n1) Demostración del cálculo de máximos y mínimos en diccionarios.\n2) Salir.\n"

def imprimirMaxMinDiccionario(listaDiccionario,max,min):
    listaDiccionario.sort()
    i=0
    listaMin=[]
    while i<min:
        listaMin.append(listaDiccionario[i])
        i+=1
    listaDiccionario.sort(reverse=True)
    i=0
    listaMax=[]
    while i<max:
        listaMax.append(listaDiccionario[i])
        i+=1
    print(f"Valores calculados en formato LISTA de Máximos: {listaMax}")
    print(f"Valores calculados en formato LISTA de Mínimos: {listaMin}")
    print(f"Valores calculados en formato TUPLA de Máximos: {tuple(listaMax)}")
    print(f"Valores calculados en formato TUPLA de Mínimos: {tuple(listaMin)}")
    return

def calcularMaxMin(diccionario):    
    continuar3=True
    while continuar3:
        num1=input("Digite el número de máximos que desea mostrar: ")
        num2=input("Digite el número de mínimos que desea mostrar: ")
        try:
            n1=int(num1)
            n2=int(num2)
            lista=list(diccionario)
            lendicc=len(diccionario)
            print(lendicc)
            if n1 >lendicc or n2 >lendicc:
                print(f"Error, número de máximos/mínimos que desea mostrar excede de la longitud del arreglo ({lendicc})")
            else:
                """Recorrer el diccionario con los valores"""
                i=0
                valores=[]
                while i<lendicc:
                    valores.append(diccionario.get(lista[i]))
                    i+=1
                imprimirMaxMinDiccionario(valores,n1,n2)
                continuar3=False
        except ValueError:
            print("Error de excepciones")
          
    return
    
def menu2():
    val_dicc1="1) {'Raul':34,'Paula':19,'Jorge':43,'Richard':10,'Diana':3,'Isabel':76,'Gustavo':12,'Diego':37}"
    dicc1={'Raul':34,'Paula':19,'Jorge':43,'Richard':10,'Diana':3,'Isabel':76,'Gustavo':12,'Diego':37}
    val_dicc2='2) {"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}'
    dicc2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
    val_dicc3='3) {"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}'
    dicc3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
    val_dicc4='4) {"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}'
    dicc4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
    opcionesDicc="\nElija un diccionario para la demostración:\n"+val_dicc1+"\n"+val_dicc2+"\n"+val_dicc3+"\n"+val_dicc4+"\n"
    continuar2=True
    while continuar2:
        opcion2=input(opcionesDicc)
        try:
            opcion2=int(opcion2)
            if opcion2 >=1 and opcion2 <=4:
                if opcion2==1:
                    calcularMaxMin(dicc1)
                elif opcion2==2:
                    calcularMaxMin(dicc2)
                elif opcion2==3:
                   calcularMaxMin(dicc3)   
                else:
                    calcularMaxMin(dicc4)                
                continuar2=False
            else:
                print("Error, opciones válidas:1,2,3 y 4")
        except ValueError:
            print("Error de excepciones")
    return

def principal():
    continuar=True
    while continuar:
        opcion=input(menu)
        try:
            opcion=int(opcion)
            if opcion==1:
                menu2()
            elif opcion==2:
                continuar=False
            else:
                print("Error, opciones válidas:1 y 2")
        except ValueError:
            print("Error de excepciones")
    return

