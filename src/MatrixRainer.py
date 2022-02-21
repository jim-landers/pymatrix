import string, random
from time import sleep

from Droplet import Droplet

class MatrixRainer:



    def __init__(self, stdscreen):

        # Screen/Window Object from curses
        self.stdscreen   = stdscreen
        # Tuple of the max coordinates (y, x)
        self.borders     = stdscreen.getmaxyx()
        self.dropletList = [] 
        for i in range(7):
            pos = self.ChooseRandPos()
            self.dropletList.insert(0, Droplet(pos))



    def LetItRain(self):
        while True:
            self.DrawDroplets()
            self.TickDroplets()
            sleep(0.1)


    def LetItDebug(self):
        print(self.dropletList[0].GetY())
        print(self.dropletList[1].GetY())
        print(self.dropletList[2].GetY())




    def ChooseRandPos(self) -> list:
        # Subtract a bit from Y to prevent drops from starting at very bottom.
        y = random.randrange(0, self.borders[0] - 4)
        x = random.randrange(0, self.borders[1])
        return [y, x]
        




    def DrawDroplets(self):
        for i in range(len(self.dropletList)):
            y = self.dropletList[i].GetY()
            x = self.dropletList[i].GetX()
            t = self.dropletList[i].GetToken()
            self.stdscreen.addstr(y, x, t)

        self.stdscreen.refresh()



    def TickDroplets(self):
        for i in self.dropletList:
            i.Tick()



