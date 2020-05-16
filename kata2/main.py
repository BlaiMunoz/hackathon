def cuadrado(y,x):
    if y == 1:
        print("funcion cuadrado")
        return x*x
    elif y == 2:
        print("funcion suma")
        return x+x
    else:
        print("error")
        return -1

def print_tupla(tup):
    for i in tup:
        print(i)


valor = 4
operacion = 2
cosa = [1,4,8,7,5,6,4,9,7,8]

print("Se va a calcular con: ",valor)
print(cuadrado(operacion,valor))

print("Se va a usar la funcion print_tupla")
print(print_tupla(cosa))