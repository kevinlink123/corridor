from constants import fuentes
from rich.console import Console
console = Console()

def printMsg(style, *mensajes, newLine=True):
        """
        Imprime los mensajes dados como argumentos con el style dado como parametro.
        El valor por default de 'style' es 'default'

        Posibles styles: default, narrador, info, exito, peligro
        """
        fuente = style
        fuenteValida = False
        for f in fuentes:
            if style == f:
                fuente = fuentes[style]
                fuenteValida = True
                break

        if not fuenteValida:
            fuente = 'default'

        for m in mensajes:
            console.print(m, style=fuente)
        if newLine == True:
            print('')