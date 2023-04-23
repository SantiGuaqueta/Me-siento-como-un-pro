# Ejercicio 10
import math

def aprox_arctan(x, n): # Define la función
    
    if abs(x) > 1: # Limita los valores que soporta
        print("Error: X debe estar en el rango [-1, 1]") # Genera el error al poner valoresfuera de los rangos
        x = float(input("Ingrese otro valor = "))
    z = 0 # Variable empieza en 0
    for i in range(0,n): # Recorre los números hasta n-1 
        a = (-1) ** i # Cambia signo y eleva por los numeros del for
        b = (x ** (2 * i + 1)) / (2 * i + 1) # Calcula una aproximación de la función arcotangente para x utilizando los primeros n términos de la serie de Maclaur
        z += a * b # Calcula todoslos datos para dar la aproximación guardada en a
    return z

if __name__ == "__main__":
    x = float(input("Ingrese el numero para calcular el ArcoTangente = ")) # Pide al usuario el número
    n = int(input("Ingrese un número de series de MacLaurin = ")) # Pide al usuario las series
    z = aprox_arctan(x, n) # Llama la función
    arctan = math.atan(x) # Valor real
    print("Resultado Serie MacLaurin: "+str(z)) # Imprime la aproximación
    print("Resultado Funcion Math: "+str(arctan)) # Imprime el valor real
    print("Diferencia: "+str(arctan - z)) # Imprime la diferencia entre los dos valores
