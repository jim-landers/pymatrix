import curses, random
from time import sleep

from Entities import Droplet, Wiper



class MatrixRainer:

    def __init__(self, stdscreen):
        # Screen/Window Object from curses
        self.stdscreen   = stdscreen
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.curs_set(0)

        # Tuple of the max coordinates (y, x)
        self.borders     = stdscreen.getmaxyx()

        self.dropletList = []
        self.wiperList   = []

        # This equates to roughly 1 droplet made for every 4 columns
        for i in range(self.borders[1] // 4):
            self.dropletList.insert(0, Droplet(self.borders))
        self.wiperList.append(Wiper(self.borders))



    def LetItRain(self):
        cycle = 0
        while True:

            self.DrawDroplets()
            self.TickDroplets()
            self.stdscreen.refresh()
            sleep(0.075)


            # This is to give the droplets some time before they start getting erased.
            # if cycle > 2:
            self.DrawWipers()
            self.TickWipers()
            if len(self.wiperList) < (len(self.dropletList) * 2):
                for i in range(random.randrange(1, 2)):
                    self.wiperList.append(Wiper(self.borders))



            self.stdscreen.refresh()
            cycle += 1
            sleep(0.075)


    def LetItDebug(self):
        test = self.wiperList[0].GetPos()
        print(test)
        self.TickWipers()
        test = self.wiperList[0].GetPos()
        print(test)

        sleep(10)


    def TrailGreen(self, drop):

        if drop.HasPrevPos():
            pos = drop.GetPrevPos()
            ch = self.stdscreen.instr(pos[0], pos[1], 1)
            self.stdscreen.addstr(pos[0], pos[1], ch, curses.color_pair(2))


    def DrawDroplets(self):
        for i in range(len(self.dropletList)):
            d = self.dropletList[i]

            self.stdscreen.addstr(d.GetY(), d.GetX(), d.GetToken())
            self.TrailGreen(d)


    def DrawWipers(self):
        for i in range(len(self.wiperList)):
            w = self.wiperList[i]
            self.stdscreen.addstr(w.GetY(), w.GetX(), ' ')




    def TickDroplets(self):
        for i in self.dropletList:
            i.Tick()


    def TickWipers(self):
        for i in self.wiperList:
            i.Tick()
