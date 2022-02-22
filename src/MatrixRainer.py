import curses
from time import sleep

from Droplet import Droplet

class MatrixRainer:



    def __init__(self, stdscreen):
        # Screen/Window Object from curses
        self.stdscreen   = stdscreen
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.curs_set(0)

        # Tuple of the max coordinates (y, x)
        self.borders     = stdscreen.getmaxyx()

        self.dropletList = [] 

        # This equates to roughly 1 droplet made for every 4 columns
        for i in range(self.borders[1] // 4):
            self.dropletList.insert(0, Droplet(self.borders))



    def LetItRain(self):
        while True:
            self.DrawDroplets()
            self.TickDroplets()
            sleep(0.15)


    def LetItDebug(self):
        print(self.dropletList[0].GetY())
        print(self.dropletList[1].GetY())
        print(self.dropletList[2].GetY())


    def TrailGreen(self, drop):

        if drop.HasPrevPos():
            pos = drop.GetPrevPos()
            ch = self.stdscreen.instr(pos[0], pos[1], 1)
            self.stdscreen.addstr(pos[0], pos[1], ch, curses.color_pair(2))


        # if (y > 0):
        #     ch = self.stdscreen.instr(y, x, 1)
        #     self.stdscreen.addstr(y, x, ch, curses.color_pair(2))




    def DrawDroplets(self):
        for i in range(len(self.dropletList)):
            d = self.dropletList[i]

            # self.stdscreen.addstr(y, x, t, curses.color_pair(2))
            self.stdscreen.addstr(d.GetY(), d.GetX(), d.GetToken())
            self.TrailGreen(d)



        self.stdscreen.refresh()



    def TickDroplets(self):
        for i in self.dropletList:
            i.Tick()



