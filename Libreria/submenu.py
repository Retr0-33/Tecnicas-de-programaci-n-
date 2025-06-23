#Libreria utilizada: Procesar, es aquella que guardo todos los datos que se introdujeron en la opción 1 y 3 del menú.
import Libreria.procesar as proc

#Se muestra al elegir la opción 2 del menú mostrando estadísticas mas especificas segun la opción que se elija
def submenu_estadisticas(): #Define una función llamada submenu_estadisticas.
    while True: #Crea un bucle que hace que el submenú se repita de forma indefinida hasta elegir el caso 5 para volver al menú principal.
        print("\n====== SUBMENÚ DE ESTADÍSTICAS ======") #Linea 7-12 nos imprime las opciones que tenemos disponibles.
        print("1. Total de jugadores procesados")
        print("2. Cantidad de jugadores por género")
        print("3. Jugadores DESTACADOS (más de 2000 puntos)")
        print("4. Ver todos los jugadores registrados")
        print("5. Volver al menú principal")

#Se tiene que introducir una opción valida del 1 al 5 como son mostradas en pantalla.
        opcion = input("Seleccione una opción: ")

#Linea 15 a 66 nos muestra distintos casos, donde segun cada opción elegida nos imprime la estadística que deseamos saber.
        if opcion == "1": #Indica que si se cumple el caso 1 se ejecuta el for.
            total = 0 #Se crea una variable llamada total que inicia en 0.
            for jugador in proc.datos_de_jugador: #Se inicia un bucle que recorre una lista presente en la libreria procesar.
                total = total + 1 #En cada vuelta del bucle, es decir, dato encontrado, se incrementa el contador en 1, segun cuantos jugadores procesados haya.
            print(f"\nTotal de jugadores procesados: {total}") #Se termina el bucle y nos imprime el total de jugadores procesados, Ej: Total de jugadores procesados: 2

        elif opcion == "2": #Ejecuta solo la opción 2, porque no se cumplió la condición 1/no se eligió.
            print(f"\nCantidad de hombres: {proc.contMasc}") #Nos muestra la cantidad de jugadores hombres que han sido procesados.
            print(f"Cantidad de mujeres: {proc.contFem}")#Nos muestra la cantidad de jugadoras mujeres que han sido procesadas.

        elif opcion == "3": #Ejecuta solo la opción 3, porque no se cumplió la condición 1 y 2/no se eligieron.
            print("\nJugadores DESTACADOS (más de 2000 puntos):") #Muestra un encabezado/título para la opción que elegimos.
            i = 1 #Sirve para enumerar los jugadores de la lista.
            hay_destacados = False #Booleano para saber si se encontro al menos un jugador destacado.
            for jugador in proc.datos_de_jugador: #Recorre entre los datos guardados y busca si hay algun jugador destacado.
                if jugador["destacado"]: #Si hay algun jugador destacado con el valor en True se ejecuta este bloque (Linea 33-34).
                    hay_destacados = True #(Linea 34-37) guarda los datos en variables mas sencillas de usar.
                    nombre = jugador["nombre"]
                    niveles = jugador["niveles"]
                    puntajes = jugador["puntajes"] #Es una lista de números según cada nivel jugado.
                    total = 0 #(Linea 38-40) Calcula la suma total de los puntajes obtenidos del jugador destacado.
                    for p in puntajes:
                        total = total + p
                    if niveles > 0: #(Linea 41-44)Calcula el promedio de puntajes por nivel, evitando dividir entre 0 si niveles es 0
                        promedio = total / niveles 
                    else: #Entonces se promedia a 0 y lo evita.
                        promedio = 0
                    print(f"{i}. {nombre} - Niveles: {niveles}, Total: {total}, Promedio: {promedio:.2f} DESTACADO") #Imprime los datos del jugador, con su número, nombre, niveles, total de puntos y promedio.
                    i = i + 1
            if not hay_destacados: #Si no encontró ningun jugador destacado en la lista, imprime No hay jugadores destacados (Linea 47-48)
                print("No hay jugadores destacados.")

        elif opcion == "4": #Ejecuta solo la opción 4, porque no se cumplió la condición 1, 2 y 3/no se eligieron.
            print("\n=== Lista de todos los jugadores registrados ===") #Imprime un título y acto seguido muestra las estadísticas que le pedimos.
            if proc.datos_de_jugador == []: #Verifica en la lista de jugadores procesados
                print("No hay jugadores registrados.") #Si no hay ninguno imprime este mensaje
            else: #Si hay jugadores, los cuales empieza a contar desde 1
                contador = 1 
                for jugador in proc.datos_de_jugador: #Recorre los datos guardados de cada jugador en la lista y muestra sus estadísticas (Linea 56-60)
                    nombre = jugador["nombre"]
                    genero = jugador["genero"]
                    niveles = jugador["niveles"]
                    puntajes = jugador["puntajes"]
                    total = 0 #Suma los puntajes totales de cada jugador procesado (Linea 61-63)
                    for p in puntajes: 
                        total = total + p
                    destacado = "Sí" if jugador["destacado"] else "No" #Condiciones, verifican si hay jugadores destacados o no y lo muestra en Destacado: {destacado} del print que vemos abajo.
                    print(f"{contador}. {nombre} | Género: {genero} | Niveles: {niveles} | Puntaje total: {total} | Destacado: {destacado}")
                    contador = contador + 1 #Suma 1 al número del jugador para el siguiente en la lista.
        elif opcion == "5": #Ejecuta solo la opción 5, porque no se cumplió la condición 1, 2, 3 y 4/no se eligieron.
            print("Volviendo al menú principal\n") #Imprime la frase volviendo al menú principal.
            break #Se rompe el bucle y vuelve al menú principal
        else: #Si no se eligio ninguna opción entera se ejecuta este bloque (Línea 70-71)
            print("Opción inválida. Intente nuevamente.") #Imprime Opción inválida, Intente nuevamente y se repite el sub menú hasta que elijamos una de las condiciones de arriba del 1 al 5.
