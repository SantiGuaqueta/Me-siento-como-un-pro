# Ejercicio 2 medio pro
range(1,1001) # Declaramos rango
pares:int # declaramos variables pares e impares que son enteros 
impares:int
for x in range(1,1001):# Usamos el for el cual tiene el rango que antes declaramos
    if x%2: # Colocamos un condicional para hallar impares 
        print(" impar : " + str(x))
    else: # si no se cumple el anterior condicional se hallara los pares
        print("par : " + str(x))
    