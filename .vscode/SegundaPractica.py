#cadena de caracteres
nombre = input ("introduce tu nombre: ")
print( f"hola {nombre}")

# entero
edad = 25 
# flotante - decimales
altura = 1.75

#convertir flotante
edadString = str(edad)

print (edad+ edad)
print (edadString + edadString)

print(type (edad))

tuEdad = input("introduce tu edad: ")
tuEdad = int(tuEdad)

if tuEdad >= 18 and tuEdad < 100:
    print("Eres mayor de edad")
elif tuEdad >= 100:
    print("Eres inmortal")
elif tuEdad <= 0:
    print("no existes")
else:
    print("eres menor de edad")

#
    for i in range(0,10):