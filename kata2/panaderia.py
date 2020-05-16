"""
Este programa calcula el precio total de la venta
pan del dia anterior
"""

precio = 3.49
descuento = 0.4
precio_con_descuento = precio * descuento

barras_pan = int(input("¿Cuántas barras de pan se han vendido? "))
print(barras_pan)

print("Precio del día %.2f" % precio + "€")
print("Precio con descuento: %.2f" % precio_con_descuento  + "€")
print("Coste total: " + str(precio_con_descuento * barras_pan)  + "€")
