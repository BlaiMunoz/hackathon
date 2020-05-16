

edad = input("Introducir edad: ")
edad = int(edad)

if edad < 0:
    print("Error, la edad no puede ser negativa, no puedes tener " + str(edad) + " años")    
elif edad < 4:
    print("El precio es 0€")
elif 4 <= edad < 18:
    print("El precio es 5€")
elif edad >= 18  and edad < 120:
    print("El precio es 10€")
else:
    print("¿Seguro que has introducido bien la edad? " + str(edad) + " años parece mucho")