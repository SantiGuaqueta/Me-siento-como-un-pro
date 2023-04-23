# Ejercicio 5
n=int (input("escriba un numero entero: ")) # Le pedimos un numero cualquiera 
range(1,n+1) # Declaramos el rango el n+1 es para que tome el valor de n
i:int=1 # Declaramos variable i como un entero y que es 1


for x in range(1,n+1): # Usamos el for co el rango indicado anteriormene
    i= i*2 # Declaramos que al operar este for el i se debe multiplicar por 2 
print("el numero 2 elevado a la " + str(n) + " es igual a " + str(i)) # En este caso el print no debe ir dentro del for imprimimos
    
    