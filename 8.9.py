# Ejercicio 9
import math

def aprox_seno(x, n): # Define la función
    z = 0
    for i in range(0,n): # Recorre todos los números hasta n-1 
        a = (-1) ** i # Cambia signo y eleva por los numeros del for
        b = (x ** (2 * i + 1)) / math.factorial(2 * i + 1) # Calcula una aproximación de la función seno para x utilizando los primeros n términos de la serie de Maclaurin
        z += a * b # Calcula todos los datos para dar la aproximación guardada en a
    return z

if __name__ == "__main__":
    x = float(input("Ingrese el numero para calcular el Seno = ")) # Pide al usuario el número
    n = int(input("Ingrese un número de series de MacLaurin = ")) # Pide al usuario las series
    z = aprox_seno(x, n) # Llama la función
    seno = math.sin(x) # Resultado real
    print("Resultado Serie MacLaurin: "+str (z)) # Imprime la aproxcimación
    print("Resultado Funcion Math: "+str(seno)) # Imprime la el valor real
    print("Diferencia = "+str(seno - z)) # Imprimir la diferencia entre los dos valores