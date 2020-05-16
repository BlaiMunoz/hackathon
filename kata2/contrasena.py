"""
Este programa verifica la contraseña introducida
por el usuario
"""

password = "contraseña"

validate = input("introducir contraseña: ")
validate = validate.lower()

if(validate == password):
    print("Contraseña correcta: " + validate)
else:
    print("contraseña incorrecta")