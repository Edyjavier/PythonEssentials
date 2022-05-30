# -*- coding: utf-8 -*-
"""
Ejercicios de Python

Created on Mon May 23 11:34:44 2022

@author: Edison Tamayo
"""

"""Desarrollar un programa que permita validar la contraseña introducida por un usuario con las 
siguientes comprobaciones:
- Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.
- Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.
- Debe contener al menos un número entre 0 y 9.
- Debe contener un símbolo especial entre: $,%,*,@
- Tamaño mínimo de 5 caracteres y máximo de 15."""
print("Indicaciones para una contraseña válida:\nDebe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.\n- Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.\n- Debe contener al menos un número entre 0 y 9.\n- Debe contener un símbolo especial entre: $,%,*,@\n- Tamaño mínimo de 5 caracteres y máximo de 15.\n") 
clave=input("Ingrese una contraseña: ")
minValidas=['a','b','c','d','e','f','g','h','i','j']
banderaMinus=False
mayValida=["K","L","M","N","O","P","Q","R","S","T"]
banderaMayus=False
numerosValidos=list(range(10))
banderaNumeros=False
simEspecValido=["$","%","*","@"]
banderaSimbol=False
longitud=(len(clave))

if longitud<5 or longitud>15:
    print(f"Contreseña inválida: Tamaño mínimo de 5 caracteres y máximo de 15, su longitud es de {len(clave)} caracteres")
else:   
    for valor in clave:
        if valor in minValidas:
            banderaMinus=True
        if valor in mayValida:
            banderaMayus=True
        if valor in str(list(range(10))):
            banderaNumeros=True
        if valor in simEspecValido:
            banderaSimbol=True    
    if (banderaMinus and banderaMayus and banderaSimbol and banderaNumeros):
        print ("Contraseña válida")        
    else:        
        print("Contreseña inválida, no cumple las condiciones:\n")
        if banderaMinus==False:
            print("- Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.")
        if banderaMayus==False:
            print("- Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.")
        if banderaNumeros==False:
            print("- Debe contener al menos un número entre 0 y 9.")
        if banderaSimbol==False:
            print("- Debe contener un símbolo especial entre: $,%,*,@")
