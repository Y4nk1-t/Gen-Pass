import random
import string

print("|||||||-ESTE ES MI GENERADOR DE CONTRASEÑAS-|||||||")
print("                        by Y4nk1")
print() 


tamaño = int(input("Cantidad de caracteres: "))
n = int(input("Cuantas contraseñas deseas: "))
decision = input("Deseas agregar signos de puntuacion? Si/No: ")
decision = decision.capitalize()


caracterespun = string.ascii_letters + string.digits
caracteres = string.ascii_letters + string.digits + string.punctuation
if decision == "Si":
    caracteres = string.ascii_letters + string.digits + string.punctuation
else:
    caracteres = string.ascii_letters + string.digits


fichero = open("generacontraseñas.txt", "w")
for lineas in range(0,n):  
    fichero.write("".join(random.choice(caracteres) for _ in range(tamaño)))
    fichero.write("\n")

fichero.close()
