# Ejercicio 8
import math

def aprox(x,n):
    m:int=0 # Declaramos variable que empieza en 0
    for y in range(n): # Declaramos rango 
         m += x**y / math.factorial(y) #Declaramos que dentro del for se realiza la serie de Maclaurin
    return m

if __name__ == "__main__":
     x= float (input("Escriba un numero = ")) #Pide un número cualquiera
     n= int (input("Escriba el numero de series de MacLaurin ="))  #Pide el número de series con el que trabajermos
     a = aprox(x ,n) # Llama la función de aproximación
     r= math.exp(x) # Toma el valor real 
     print(a) # Imprime la aproximación
     print(r) # Imprime el valor real
     print("La diferencia = "+str(r-a)) # Imprime la diferencia entre los dos valoes
