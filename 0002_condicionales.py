a = 10

if a == 10:
    print("Es 10")
else:
    print("No es 10")


# Decimales y cadenas
valor_decimal = 10.3234

# Cadenas
mi_cadena = "Hola mundo"

# Ejercicio aritmetico
# Deinimos una variable x con una cadena
x = "El valor de (a+b)*c es"

# Podemos realizar multiples asignaciones
a, b, c = 4, 3, 2

# Realizamos operacion con a, b, c
d = (a + b) * c

# Definimos una variable booleana
imprimir = True

# Si imprimir, print()
if imprimir:
    print(x, d)

# Salida: Evalor de (a+b)*c es 14

"""
Este es un bloque de codigo 
que es un comentario con varias
lineas
"""

# Codigo a ejecutarse con varias lineas
x = 1 + 2 + 3 + 4 +\
5 + 6 + 7 + 8

print("x: ", x)


# Crear variables y asignarles el mismo valor
x = y = z = 10

# Crear varios valores y asignarles diferentes valores separados por comas
x, y = 4, 2
a, b, c = 1, 2, 3

# Ejemplo de variable pasada por valor
# Se crea una copia interna de la varaible entregada a la funcion
# Esto hace que se trabaje sobre la copia, dejando la variable original intacta
x = 10

def funcion(entrada):
    entrada = 0

funcion(x)

print(x) # 10


# Ejemplo de paso por referencia
x = [10, 20, 30]
def funcion2(entrada):
    entrada.append(40)

funcion2(x)
print(x) # [10, 20, 30, 40]

# Trabajando con el id unico de una variable

x = [10,20,30]
print("El id de la variable x: ",id(x)) 

def funcion3(entrada):
    entrada.append(40)
    print("id unico de entrada: ",id(entrada)) # El mismo id que el de la variable x

funcion3(x)

