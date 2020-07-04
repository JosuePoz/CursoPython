from random import random
import time

def Vencedor (ganador):
    if (ganador == "1"):
        return "Piedra Vence Tijera"
    elif (ganador == "2"):
        return "Tijera Vence Papel"
    else:
        return "Papel Vence Piedra"

print("Bienvenido a piedra, papel, extremo >=v")
i = 1
while i > 0:
    print ("Elige numero de opcion:")
    print ("Piedra  =   1")
    print("Tijera   =   2")
    print("Papel    =   3")
    jugador = input()
    Computadora =  str(round(1+ random()*2))
    if jugador == Computadora:
        print ("Es un empate, buen juego crack")
    else:
        if (jugador == "1" and Computadora == "2") or (jugador == "2" and Computadora == "3") or (jugador == "3" and Computadora =="1"):
            print ("Ganaste master")
            print (Vencedor(jugador))
        elif (jugador == "2" and Computadora == "1") or (jugador == "3" and Computadora == "2") or (jugador == "1" and Computadora =="3"):
            print ("Gano la computadora master")
            print (Vencedor(Computadora))
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("PERDEDOR!!!!!")
        else:
            print ("Epale Epale!")
            time.sleep(0.5)
            print ("Eso no se puede campeon")
            print(Computadora)
    i = int(input("Desea seguir jugando? 0 = No, 1 = Si "))
    print("------------------------------------------")
print("Muchas gracias por jugar, vuelve pronto ;) ;)")
print ("Proximamente... piedra papel tijera lagarto spock")