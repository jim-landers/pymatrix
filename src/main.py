from curses import wrapper
from time import sleep


from MatrixRainer import MatrixRainer




def main(stdscreen):
    matrixRainer = MatrixRainer(stdscreen)
    matrixRainer.LetItRain()


# Executes main in a curses wrapper() to ensure a clean program termination.
wrapper(main)

