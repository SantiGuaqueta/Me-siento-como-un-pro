# Ejercicio 2 nada pro
range(1,501) #agrego un rango pero este no ira hasta 100
pares:int=2 # Declaramos dos variables pares e impares los cuales son enteros y pares tendra valor de 2 e impares valor de 1
impares:int=1
for x in range(1,501): # Usamos el for con el rango 
    print("Los numeros pares son:" + str(pares) + " y los impares " + str(impares)) # Imprimimos pares e impares
    impares += 2 # Le pedimos que sume dos al valor que declaramos en impares lo mismo con pares 
    pares += 2
# Es una forma no tan pro debido a que tomamos un rango que no sea 1000 que fue el pedido pues en esta forma solo sumamos no saltamos valores