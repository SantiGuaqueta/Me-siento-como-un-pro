# Ejercicio 6
n=int (input("escriba un numero entero: "))# Le pedimos un numero cualquiera este es el numero que se elevara este debe ser entero
x=float (input("escriba un numero: ")) # Le pedimos un numero que sea el que vamos a elevar por el numero n dado este si es un flotante
range(1,n+1) # Declaramos el rango que queramos en este caso con n+1 para que tome el valor de n
y:float # Declaramos la variable y, la cual es un flotante en este caso


for z in range(1,n+1): # Usamos el for el con el rango anteriormente nombrado
    y= x**n # Dentro de este for y la variable que pusimos antes sin valor es igual a la operacion de x elevado a la y
print("el numero" + str(x) + " elevado a la " + str(n)+" es igual a "+ str(y)) # Print fuera del for para empezar e imprimimos la variables deseadas 
    