from random import randint
from time import sleep

from Auxiliares import printMsg


class Personaje:
    def __init__(self):
        self.nombre = ''
        self.salud = 1
        self.saludMax = 1
        self.fuerza = 1
        self.defensa = 1
        self.modo = 'ataque' #'ataque': no aumenta la defensa,'defensa': aumenta en 2 la defensa hasta que se ataque 
        self.estaVivo = True
    
    def atacar(self, enemigo):
        printMsg("info", f'{self.nombre} ataca', newLine=False)
        self.modo = 'ataque'
        sleep(1.0)

        #TODO: Decidir si implementar un danio minimo hacia cualquier entidad
        danio = min(max(self.fuerza - enemigo.defensa + randint(-2 , 3), 0), self.salud)
        if enemigo.modo == 'defensa':
            danio -= 2
        
        #TODO: Agregar mecanica de esquiva 
        if danio <= 0:
            printMsg("default" ,f'{enemigo.nombre} esquiva el ataque!')
        else:
            printMsg("default" ,f'{danio} puntos de daño causados')

        sleep(1.0)

        enemigo.salud = enemigo.salud if danio <= 0 else enemigo.salud - danio
        if(enemigo.salud <= 0):
            enemigo.morir()

    def morir(self):
        self.estaVivo = False

    def estado(self, enemigo):
        print("Jugador: ")
        print("nombre: ", self.nombre)
        print("salud: ", self.salud)
        print("esta vivo: ", self.estaVivo)
        print("fuerza: ", self.fuerza)
        print(" ")

        print("Enemigo: ")
        print("nombre: ", enemigo.nombre)
        print("salud: ", enemigo.salud)
        print("esta vivo: ", enemigo.estaVivo)
        print("fuerza: ", enemigo.fuerza)
        print(" ")
    
    def suicidio(self, enemigo):
        self.salud = 0
        self.estaVivo = False

    
    def defender(self, enemigo):
        print(f'{self.nombre} se esta defendiendo')
        self.modo  = 'defensa'