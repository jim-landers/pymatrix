import os
from os import system, name

from Rainer import Rainer


def ClearTerminal():
    # Windows
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


if __name__ == "__main__":
    ClearTerminal()
    termDims = os.get_terminal_size()




    rainer = Rainer(termDims)

    rainer.LetItRain()




