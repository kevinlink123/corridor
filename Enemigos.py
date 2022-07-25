from Personaje import Personaje

class Enemigo(Personaje):
    def __init__(self):
        Personaje.__init__(self)
        self.nombre = "Slime"
        self.salud = 3
        self.saludMax = 3

class Slime(Enemigo):
    def __init__(self):
        Enemigo.__init__(self)
        self.nombre = "Slime"
        self.salud = 2
        self.saludMax = 3
        self.fuerza = 1
        self.defensa = 0

class Esqueleto(Enemigo):
    def __init__(self):
        Enemigo.__init__(self)
        self.nombre = 'Esqueleto'
        self.salud = 5
        self.saludMax = 5
        self.fuerza = 2
        self.defensa = 1

class Goblin(Enemigo):
    def __init__(self):
        Enemigo.__init__(self)
        self.nombre = 'Goblin'
        self.salud = 4
        self.saludMax = 4
        self.fuerza = 1
        self.defensa = 1

listaDeEnemigos = [Slime, Esqueleto, Goblin]