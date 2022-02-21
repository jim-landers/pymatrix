import curses
from curses import wrapper
from time import sleep


from MatrixRainer import MatrixRainer




def main(stdscreen):
    matrixRainer = MatrixRainer(stdscreen)
    matrixRainer.LetItRain()
    # matrixRainer.LetItDebug()



    # Test Zone start

    # Test Zone end



wrapper(main)


