"""
args y kwargs:
Vamos a suponer que queremos una funcion que sume un conjunto de numeros, pero no sabemos
a priori la cantidad de números que se quieren sumar. Si por ejemplo tuvieramos tres,
la funcion sería tan sencilla como la siguiente
"""

def suma(a,b,c):
    return a+b+c

result = suma(2,4,6)

print("result: ",result)# Salida: 12

# Si queremos sumar 4 numeros entonces se obtendrá un error
# result2 = suma(2,4,6,1)
# print(result2) # Error

# Uso de args
def suma2(*args):
    s = 0
    for arg in args:
        s += arg
    
    # imprimir el tipo de args
    print("Tipo de args: ", type(args))

    return s

print("Resultado con args: ", suma2(1,2,3,4,5,6,7))
print("Resultado con args: ", suma2(1,1, 22))


# Obteniendo el tipo de los args
# print("Tipo de args: ", type(*args))



