from PIA_CLASS import Agregar

print(f"{'*'*9} BIENVENIDO AL CREADOR DE FRASES {'*'*9}")
print(f"{'*'*20} MENU {'*'*20}")
print("1.-Agregar Frase\n2.-Ver Frase\n3.-Ver Frases\n4.-Eliminar Frase\n5.-Modificar Frase\n6.-Salir")

op = int(input("Elija una opcion>> "))
frases = []

if op == 1:
    id = int(input("Ingresa el identificador de la frase>> "))
    frase = input("Escribe la frase>> ")
    autor = input("El nombre del autor es>> ")
    cal = int(input("Dale una calificacion a la frase>> "))
    frase = Agregar(frase,autor,cal,id)
    frase.agregar_frase

