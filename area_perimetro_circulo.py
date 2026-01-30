# Programa para calcular el area y el perimetro de un circulo 
import math
print("-----------------------------")
print("Area y perimetro del cirfculo")
print("-----------------------------")
r= input("Digite el valor del Radio ")
r=int(r)

#---------
#procesing
#---------

a= math.pi*r*r
p=2*math.pi*r

#------
#salida
#------
print("------------------")
print("Los resultados son:")
print("------------------")

print("El area de el circulo es:"+str(a))

print("El valor de el perimetro es:"+str(a))

print("-----------------------------")
print("Gracias por su comprencion :)")
print("-----------------------------")