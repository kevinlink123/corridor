from Auxiliares import printMsg
from Enemigos import Enemigo
from Jugador import Jugador
from rich.console import Console
console = Console()

from constants import accionesDisponibles, acciones, fuentes

class Combate:
    def __init__(self, jugador: Jugador, enemigo: Enemigo):
        self.turnoActual = 0 #0: Jugador, 1: Enemigo/s
        self.turnos = 1
        self.jugador = jugador
        self.enemigo = enemigo

        self.combateTerminado = False

        printMsg("info" ,f'Comandos disponibles')
        self.ayuda()

    def ayuda(self):
        for accion, descripcion in accionesDisponibles.items():
            console.print(f'[reverse]{accion}[/reverse]: [white]{descripcion}[/white]', style='green')
        print("")

    def estado(self):
        print(f'{self.jugador.nombre}: {self.jugador.salud}', end=" VS ")
        for e in self.enemigos:
            print(f'{e.nombre}: {e.salud}')

    def turnoFinalizado(self):
        if self.turnoActual == 0:
            self.turnoActual = 1
        else:
            self.turnoActual = 0

    def actualizarEstado(self):
        #El combate finaliza cuando cualquiera de los personajes muere
        self.combateTerminado = True if not self.jugador.estaVivo or not self.enemigo.estaVivo else False
        

    def iniciarCombate(self):
        while not self.combateTerminado:
            #Turno del jugador
            if self.turnoActual == 0:
                print(f'Turno de {self.jugador.nombre}')
                #Input de accion del jugador
                accionInput = input("> ")

                #Accion del jugador
                accionEncontrada = False
                for a in acciones:
                    if accionInput == a:
                        accionEncontrada = True
                        #Se ejecuta la accion del jugador
                        accion = getattr(self.jugador, accionInput)
                        accion(self.enemigo)
                        
                        #Se finaliza el turno del jugador y se actualiza el estado del combate
                        if(accionInput != 'estado'):
                            self.turnoFinalizado()
                            self.actualizarEstado()
                        break

                
                if not accionEncontrada:
                    print("Accion invalida")
            #Turno del enemigo
            elif self.turnoActual == 1:
                #Accion del enemigo
                #Se ejecuta la accion del enemigo
                self.enemigo.atacar(self.jugador)

                #Se finaliza el turno del jugador y se actualiza el estado del combate
                self.turnoFinalizado()
                self.actualizarEstado()
        
        #El combate termino
        print(f'Combate finalizado')

        if not self.jugador.estaVivo:
            print(f'Tu vida llego a su fin...')
            return False

        elif not self.enemigo.estaVivo:
            print(f'Enemigos abatidos!')
            printMsg("default","La alegria de seguir respirando...")
            return True