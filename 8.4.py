#Ejercicio 4
n=int (input("escriba un numero entero: ")) # Le pedimos un numero cualquiera 
range(1, n+1) # Declaramos el rango el n+1 es para que tome el valor de n
factorial:int=1 # Declaramos la variable en este caso con nombre factorial el cual decimos que es un entero y que es igual a 1

for x in range(1,n+1): # Usamos el for con el rango anteriormente nombrado
    factorial *= x # Dentro del for ponemos esto lo cual indica que mientras se opere el for el factorial se multiplica por x
    print("Los numero son "+ str(x) +" y sus factoriales son " + str(factorial)) # En este caso el print si hiria dentro del for para que con cada valor del frango que tiene el for se halle el factorial