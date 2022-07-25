import random
from time import sleep
from random import randint
from typing import List

#Permitir el uso de la libreria Rich en windows
from colorama import init
from rich.console import Console

console = Console()

#Constantes
from constants import decisiones, fuentes

#Elementos del juego
from Auxiliares import printMsg
from Combate import Combate
from Jugador import Jugador
from Enemigos import Enemigo, listaDeEnemigos

class Juego:
    def __init__(self):
        self.combate = None
        self.jugador = Jugador()
        self.cuartosRestantes = 10
        self.antorchaEncendida = False

        self.decision = False
        self.run = False

    def crearCombate(self):
        enemigo = random.choice(listaDeEnemigos)()
        self.combate = Combate(self.jugador, enemigo)
        jugadorSigueVivo =  self.combate.iniciarCombate()

        if not jugadorSigueVivo:
            self.run = False
            return

        printMsg("info", 
        f'[bold]{self.jugador.nombre}[/bold]',
        f'Salud: {self.jugador.salud}/{self.jugador.saludMax}',
        f'Fuerza: {self.jugador.fuerza}'
        )

        printMsg("info",
            "[reverse]caminar[/reverse], [reverse]descansar[/reverse] o manipular [reverse]antorcha[/reverse]"
        )

    
    def caminar(self):
        resultado = randint(1, 6)
        if resultado < 4:
            printMsg("peligro", "Hay un enemigo adelante!")
            self.crearCombate()

        elif resultado >= 4:
            printMsg("info", 
            "La sala esta vacia"
            )

    def descansar(self):
        if self.jugador.salud >= self.jugador.saludMax:
            printMsg("info","No podes descansar si no estas cansado")
            return
        
        printMsg("narrador", "Te sentas en el suelo contra una pared.", "sientes que se alivia tu carga...")
        self.jugador.salud = self.jugador.salud + 2 if self.jugador.salud + 2 < self.jugador.saludMax else self.jugador.saludMax
        printMsg("info", f'Vida actual: {self.jugador.salud}')

    def antorcha(self):
        self.antorchaEncendida = not self.antorchaEncendida
        msg = 'Enciendes la antorcha' if self.antorchaEncendida else 'Apagas la antorcha'
        printMsg("info", msg)

    
    def mainLoop(self):
        self.run = True
        printMsg("narrador", 
            "Estas dentro de un pasillo largo. Tu unica oportunidad de salir es abriendote paso entre la oscuridad...",
            "Hay una antorcha en el piso. Tu unica fuente de luz, pero encenderla podria atraer atencion indeseada",
        )
        
        console.print("Solo ves 3 posibles acciones:")
        printMsg("info",
            "[reverse]caminar[/reverse], [reverse]descansar[/reverse] o encender la [reverse]antorcha[/reverse]"
        )

        #Empieza el juego en si
        #Esta primera seccion trata de seguir el camino adentrandose en el monte.
        while self.run:
            decisionInput = input("> ")
            
            decisionValida = False
            for d in decisiones:
                if decisionInput == d:
                    decisionValida = True
                    decision = getattr(self, decisionInput)()
                    break
            
            if not decisionValida:
                printMsg("peligro", "Decision invalida")

juego = Juego()

juego.mainLoop()