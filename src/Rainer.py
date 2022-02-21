import random
import string
from time import sleep



string.CHARS = "!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"

class Rainer:

    def __init__(self, termDims):
        self.width  = termDims.columns
        self.length = termDims.lines



    def PrintDimensions(self):
        print(f"Rainer width : {self.width}")
        print(f"Rainer length: {self.length}")


    def GenerateRandChar(self) -> str:
        randChar = random.choice(string.CHARS)
        return randChar


    def GenerateCharRow(self) -> list:
        charRow = [''] * self.width

        for i in range(len(charRow)):
            charRow[i] = self.GenerateRandChar()

        # print(*charRow, sep='', end='\n')
        return charRow


    def LetItRain(self):
        while True:
            print(*self.GenerateCharRow(), sep='', end='\n')
            sleep(1)



